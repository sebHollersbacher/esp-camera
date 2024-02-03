import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import mqtt from 'mqtt';

export default function Image() {
  const [img, setImage] = useState('');
  const { image } = useParams();
  let navigate = useNavigate();

  useEffect(() => {
    fetchImage();
  }, []);

  const handlePublish = () => {
    const client = mqtt.connect("ws://192.168.178.48:9001")
    client.on('connect', () => {
      console.log("connected")
      client.publish("esp_cam_0", "esp_cam_0");
      client.end();
    });
  };

  const fetchImage = () => {
    fetch('/uploads/' + image)
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
      <button onClick={() => navigate(-1)}>Back</button> 
      <button onClick={handlePublish}>MQTT</button>
      <br/>
      {image && <img src={img} alt='img'/>}
    </div>
  );
}
