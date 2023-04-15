import React from 'react';
import { Background, LoadingText } from './Styles';
import Spinner from './Spinner.gif'

function Loading() {
  return (
    <Background>
      <LoadingText style={{
        fontSize: "25px",
        fontWeight: "bold",
        fontFamily: "BMJUA",
      }}>
        해시태그 생성 중 . . .
      </LoadingText>
      <img src={Spinner} alt="로딩중" width="5%" />
    </Background>
  );
}

export default Loading;