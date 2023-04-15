import React from "react";
import "./ImageForm.css";

function ImageForm({onChange, onClick}) {

  return (
    <div className="input-form">
      <div className="image-form">
        <form onChange={onChange}>
          <input
            type='file'
            accept='image/jpg,image/jpeg,image/gif'
            name='image'
            id='image'
          />
        </form>
      </div>
      <div className="create-button" onClick={onClick}>
        해시태그 생성하기
      </div>
    </div>
  );
}

export default ImageForm;