import { useEffect, useState } from 'react';
import mqtt from 'mqtt';

export default function ImageList() {
  const [result, setResult] = useState([]);

  useEffect(() => {
    getImageList();
  }, []);

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

  const handlePublish = () => {
    const client = mqtt.connect("ws://192.168.178.48:9001")
    client.on('connect', () => {
      console.log("connected")
      client.publish("esp_cam_0", "esp_cam_0");
      client.end();
    });
  };

  return (
    <div>
      <button onClick={handlePublish}>MQTT</button>
      <button onClick={getImageList}>Get Image List</button>
      <ul>
        {result.map((image) => (
          <li key={image}>
            <a href={image}>{image}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
