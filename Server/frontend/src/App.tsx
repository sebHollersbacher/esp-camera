import React, { useState } from 'react';
import './App.css';

export default function App() {
  const [result, setResult] = useState([]);
  const [image, setImage] = useState('');

  const getImageList = () => {
    fetch('/files')
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        setResult(data);
      });
  };

  const fetchImage = () => {
    fetch('/uploads/frog.jpg')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Could not get image');
        }
        return response.blob();
      })
      .then((blob) => {
        const imageUrl = URL.createObjectURL(blob);
        setImage(imageUrl);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
    <button onClick={fetchImage}>Get Image</button>
      <button onClick={getImageList}>Get Image List</button>
      {result && (
        <div>
          <h2>Images:</h2>
          <pre>{JSON.stringify(result)}</pre>
        </div>
      )}
      {image && <img src={image} alt='img'/>}
    </div>
  );
}
