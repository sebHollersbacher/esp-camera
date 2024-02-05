import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Page from './Page';
import Image from './Image';



function App() {


    return (
        <Router>
          <Routes>
            <Route path="/" element={< Page />} />
            <Route path=":image" element={< Image />} />
          </Routes>
        </Router>
      );
}

export default App;