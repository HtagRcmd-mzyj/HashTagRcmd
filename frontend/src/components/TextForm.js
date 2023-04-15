import React from "react";
import "./TextForm.css";

function TextForm({onClick}) {
  return (
    <div className="input-form">
      <div className="text-form">
        <textarea
          placeholder='텍스트를 입력하세요'
          name='text'
          id='input_text'
        />
      </div>
      <div className="create-button" onClick={onClick}>
        해시태그 생성하기
      </div>
    </div>

  );
}

export default TextForm;

