import { useEffect, useState } from 'react';
import TakeImageButton from './TakeImageButton';
import SyncButton from './SyncButton';
import AllImages from './AllImages';



export default function Page() {
  const [result, setResult] = useState([]);

  useEffect(() => {
    getImageList();
  }, []);

  const getImageList = () => {
    fetch('http://192.168.0.23:8000/files')
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
    <div>
      <h1>Welcome to SnapiDepi!</h1>
      <TakeImageButton/>
      <h2>All Snapis {<SyncButton onClick={getImageList} />}</h2>
      <AllImages images={result} />
    </div>
  );
}
