import React from "react";
import "./SelectedHtag.css";


function SelectedHtag({selectedHtag, copy, setCopy}) {
  const handleCopyClipBoard = (text) => {
    try {
      const $textarea = document.createElement('textarea');
      document.body.appendChild($textarea);
      $textarea.value = text;
      $textarea.select();
      document.execCommand('copy');
      document.body.removeChild($textarea);
      setCopy(true);
    } catch (error) {
      alert("Failed Copy");
    }
  };
  return (
    <>
      <div className="selected-htag-box">
        <div className="selected-htag">
          {selectedHtag.map((htag, idx) => <span key={idx}>#{htag} </span>)}
        </div>
        <div className="copy-button"
             onClick={() => handleCopyClipBoard(document.querySelector(".selected-htag").innerText)}
        >
          {copy ? "Copied!" : "Copy"}
        </div>
      </div>
    </>
  );
}

export default SelectedHtag;
