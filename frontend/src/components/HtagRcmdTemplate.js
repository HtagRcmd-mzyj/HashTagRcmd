import React from 'react';
import './HtagRcmdTemplate.css';
import {NavLink} from "react-router-dom";


const HtagRcmdTemplate = ({form, children, children2}) => {
  return (
    <main className="main-container">

      <header className="header">
        해시태그 자동 추천 시스템
      </header>

      <div className="htag-rcmd-template">
        <div className="select-container">
          <NavLink to="/image" className={({isActive}) => (isActive ? "select-box" : "non-select-box")}>
            이미지로 추출하기
          </NavLink>
          <NavLink to="/text" className={({isActive}) => (isActive ? "select-box" : "non-select-box")}>
            텍스트로 추출하기
          </NavLink>
        </div>
        <div className="form-wrapper">
          {form}
        </div>
        <div className="htag-wrapper">
          <div className="show-wrapper">
            {children}
          </div>
          <div className="select-wrapper">
            {children2}
          </div>
        </div>
      </div>
    </main>
  );
};

export default HtagRcmdTemplate;