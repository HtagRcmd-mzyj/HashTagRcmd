import React from 'react';
import './HtagRcmdList.css';


function HtagRcmdList({hashtag, checkedList, setCheckedList, copy, setCopy}) {
  const crawledHashtag = hashtag;
  const ARR_HASHTAG = crawledHashtag.split(' ');

  const onCheckedElement = (checked, item) => {
    if (checked) {
      setCheckedList([...checkedList, item]);
    } else if (!checked) {
      setCheckedList(checkedList.filter((el) => (el) !== item));
    }
  };


  return (
    <div className="htag-item">
      {ARR_HASHTAG.map((item, index) => {
          return (
            <div className="ListHashtagStatus" key={index}>
              <input
                type="checkbox"
                value={item}
                onChange={(e) => {
                  //onChange이벤트 발생시 check여부와 value(data)값을 전달해,
                  onCheckedElement(e.target.checked, e.target.value);
                  if (copy === true ) {
                    setCopy(prev => !prev);
                  }
                }}
                // 체크표시 해제를 시키는 로직. 배열에 data가 있으면 true, 없으면 false
                checked={checkedList.includes(item)}
              />
              <span className="htag-items">#{item} </span>
            </div>
          )
        })}
    </div>
  );
}

export default HtagRcmdList;