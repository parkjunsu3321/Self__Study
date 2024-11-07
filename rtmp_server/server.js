const express = require('express');
const NodeMediaServer = require('node-media-server');

// 허용된 스트리밍 키 목록
const VALID_STREAM_KEYS = new Set([
  'stream-key-1',
  'stream-key-2',
  'test-key'
]);

const config = {
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
  },
  trans: {
    ffmpeg: './ffmpeg', // ffmpeg 경로
    tasks: [
      {
        app: 'live',
        hls: true,
        hlsFlags: '[hls_time=2:hls_list_size=3:hls_flags=delete_segments]',
        hlsKeep: true,
        dash: true,
        dashFlags: '[f=dash:window_size=3:extra_window_size=5]',
        dashKeep: true,
        rtmp: true, // RTMP 출력 활성화
        rtmpApp: 'live_rtmp', // RTMP 출력 스트림의 경로
      }
    ]
  },
  auth: {
    api: true,
    api_user: 'admin',
    api_pass: 'admin123',
  }
};

const nms = new NodeMediaServer(config);

// Express 앱 설정
const app = express();
const PORT = 3000;

// 스트리밍 키 검증 함수
function validateStreamKey(streamKey) {
  return VALID_STREAM_KEYS.has(streamKey);
}

// 스트림 경로에서 키 추출하는 함수
function getStreamKeyFromPath(streamPath) {
  const parts = streamPath.split('/');
  return parts[parts.length - 1];
}

// 스트리밍 시작 전 인증
nms.on('prePublish', (id, StreamPath, args) => {
  const streamKey = getStreamKeyFromPath(StreamPath);
  console.log('[StreamKey Check]', streamKey);

  if (!validateStreamKey(streamKey)) {
    const session = nms.getSession(id);
    session.reject();
    console.log('[StreamKey Check] Invalid key:', streamKey);
  } else {
    console.log('[StreamKey Check] Valid key:', streamKey);
  }
});

// Express 라우팅 예시
app.get('/', (req, res) => {
  res.send('미디어 서버에 오신 것을 환영합니다!');
});

// 서버 시작
nms.run();
app.listen(PORT, () => {
  console.log(`Express 서버가 ${PORT} 포트에서 실행 중입니다.`);
});
console.log('미디어 서버가 시작되었습니다.');
console.log('RTMP 서버: rtmp://localhost:1935/live');
console.log('HTTP 서버: http://localhost:8000/live');
console.log('허용된 스트림 키:', Array.from(VALID_STREAM_KEYS));