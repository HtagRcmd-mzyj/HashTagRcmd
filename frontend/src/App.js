import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Text from "./routes/Text";
import Image from "./routes/Image";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/image/" element = {<Image />}></Route>
          <Route path="/text/" element = {<Text />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}


export default App;