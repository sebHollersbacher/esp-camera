import { useEffect, useState } from 'react';
import TakeImageButton from "./components/TakeImageButton";
import SyncButton from "./components/SyncButton";
import ImageList from "./components/ImageList";



export default function Page() {
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


  return (
    <div >
      <h1>Welcome to SnapiDepi!</h1>
      <hr
        style={{
            color: "black",
            backgroundColor: "black",
            height: 1
        }}
      />
      <TakeImageButton />
      <h2>All Snapis {<SyncButton onClick={getImageList} />}</h2>
      <ImageList images={result} />
    </div>
  );
}
