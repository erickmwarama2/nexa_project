import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Assistant from "./Assistant";
import History from "./History";
import Header from "./Header";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<Assistant />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </>
  );
}

export default App;
