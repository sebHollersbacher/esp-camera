import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ImageList from './ImageList';
import Image from './Image';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={< ImageList />} />
        <Route path=":image" element={< Image />} />
      </Routes>
    </Router>
  );
}

export default App;