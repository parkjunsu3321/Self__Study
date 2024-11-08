// src/Launches.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';

const Container = styled.div`
  font-family: 'Arial', sans-serif;
  background: linear-gradient(to right, #ff7e5f, #feb47b);
  padding: 50px;
  color: white;
  min-height: 100vh;
`;

const Title = styled.h1`
  text-align: center;
  font-size: 3em;
  margin-bottom: 40px;
`;

const LaunchCard = styled.div`
  background-color: #333;
  border-radius: 12px;
  padding: 20px;
  margin: 20px auto;
  width: 80%;
  max-width: 600px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  transition: transform 0.3s;
  
  &:hover {
    transform: scale(1.05);
  }
`;

const LaunchTitle = styled.h3`
  font-size: 1.5em;
  color: #feb47b;
`;

const LaunchDate = styled.p`
  font-size: 1.2em;
  color: #f5f5f5;
`;

const LaunchImage = styled.img`
  width: 100%;
  max-width: 400px;
  border-radius: 8px;
  margin-top: 20px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
`;

const Launches = () => {
  const [launches, setLaunches] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLaunches = async () => {
      try {
        const response = await axios.get('http://localhost:8000/spacex/launches');
        setLaunches(response.data);
      } catch (error) {
        console.error("There was an error fetching the launches:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchLaunches();
  }, []);

  return (
    <Container>
      <Title>SpaceX Launches</Title>
      {loading ? (
        <p style={{ textAlign: 'center' }}>Loading...</p>
      ) : (
        <div>
          {launches.map((launch, index) => (
            <LaunchCard key={index}>
              <LaunchTitle>{launch.name}</LaunchTitle>
              <LaunchDate>{launch.date_utc}</LaunchDate>
              {launch.image_small && (
                <LaunchImage
                  src={launch.image_small}
                  alt={launch.name}
                />
              )}
            </LaunchCard>
          ))}
        </div>
      )}
    </Container>
  );
};

export default Launches;