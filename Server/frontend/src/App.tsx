import React from 'react';
import {BrowserRouter as Router, Routes, Route, useParams} from 'react-router-dom';
import Page from './Page';


function App() {
    return (
        <Router>
          <Routes>
            <Route path="/" element={< Page />} />
          </Routes>
        </Router>
      );
}

export default App;
