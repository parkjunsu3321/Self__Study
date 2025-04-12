const NodeMediaServer = require('node-media-server');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const ffmpegProcesses = {};

const config = {
  logType: 3,
  rtmp: {
    port: 1935,
    chunk_size: 60000,
    gop_cache: true,
    ping: 30,
    ping_timeout: 60
  },
  http: {
    port: 8000,
    mediaroot: './media',
    allow_origin: '*'
  }
};

const nms = new NodeMediaServer(config);

nms.on('prePublish', (session) => {
  console.log('[PrePublish]', session.streamPath);
});

nms.on('postPublish', (session) => {
  const streamPath = session.streamPath;
  const streamKey = streamPath.split('/').pop();
  const outputDir = path.join(__dirname, 'media', 'live', streamKey);

  console.log('[PostPublish]', streamPath);

  // 폴더 생성
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
    console.log(`📁 Created folder: ${outputDir}`);
  }

  // FFmpeg 명령어 실행
  const ffmpegArgs = [
    '-i', `rtmp://localhost:1935${streamPath}`,
    '-c:v', 'copy',
    '-c:a', 'copy',
    '-f', 'hls',
    '-hls_time', '2',
    '-hls_list_size', '5',
    '-hls_flags', 'delete_segments',
    path.join(outputDir, 'index.m3u8')
  ];

  console.log(`🚀 Spawning FFmpeg for ${streamKey}`);

  const ffmpegProcess = spawn('ffmpeg', ffmpegArgs);

  ffmpegProcess.stdout.on('data', (data) => {
    console.log(`[FFmpeg stdout - ${streamKey}] ${data}`);
  });

  ffmpegProcess.stderr.on('data', (data) => {
    console.error(`[FFmpeg stderr - ${streamKey}] ${data}`);
  });

  ffmpegProcess.on('close', (code) => {
    console.log(`⚠️ FFmpeg process for ${streamKey} exited with code ${code}`);
  });

  ffmpegProcesses[streamKey] = ffmpegProcess;
});

nms.on('donePublish', (session) => {
  const streamPath = session.streamPath;
  const streamKey = streamPath.split('/').pop();

  console.log('[DonePublish]', streamPath);

  const proc = ffmpegProcesses[streamKey];
  if (proc) {
    proc.kill('SIGINT');
    delete ffmpegProcesses[streamKey];
    console.log(`🛑 FFmpeg process for stream ${streamKey} stopped`);
  }
});

nms.run();
