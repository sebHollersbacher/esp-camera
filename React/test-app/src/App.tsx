import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

export default function App() {
  const[result, setResult] = useState([]);
  const controller = new AbortController();

  useEffect(() => {
    async function getData() {
      const response = await fetch('http://192.168.0.27:8000/', {signal: controller.signal});
      const data = await response.json();
      setResult(data);
    }

    getData();

    console.log(result, "result");

    return () => {
      controller.abort();
    };
  }, []);

  return (
    <div>test</div>
  );
}
