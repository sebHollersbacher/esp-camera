import { useEffect, useState } from 'react';
import mqtt from 'mqtt';

interface ImagesProps {
  image: string;
}

export default function Image({image}: ImagesProps) {
  const [img, setImage] = useState('');

  useEffect(() => {
    fetchImage();
  }, []);

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
      {image && <img src={img} alt='img' style={{ width: '50%', height: 'auto' }} /> }
    </div>
  );
}
