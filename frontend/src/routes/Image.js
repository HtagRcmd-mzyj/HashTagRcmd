import React, {useState, useEffect} from 'react';
import HtagRcmdTemplate from "../components/HtagRcmdTemplate";
import ImageForm from "../components/ImageForm";
import HtagRcmdList from "../components/HtagRcmdList";
import SelectedHtag from "../components/SelectedHtag";
import Loading from "../components/Loading";
import axios from "axios";


function Image() {
  const [keyword, setKeyword] = useState("");
  const [hashtag, setHashtag] = useState("");
  const [checkedList, setCheckedList] = useState([]);
  const [copy, setCopy] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    console.log(keyword);
  }, [keyword]);

  const handleInputImage = async (e) => {
    e.preventDefault();
    const image = document.getElementById("image").files[0];
    const formData = new FormData();
    formData.append('image', image, image.name);
    console.log(formData) // FormData {}
    for (const keyValue of formData) console.log(keyValue);     //["img", File] File은 객체
    axios
      .post("http://127.0.0.1:8000/image/image_model/saveimg/", formData, {
        headers: {
          'content-type': 'multipart/form-data'
        }
      })
      .then(function (response) {
        console.log(response);
        const uploadImgObj = response.data;
        const imgPath = uploadImgObj[Object.keys(uploadImgObj)[1]];
        console.log(imgPath);

        axios
          .get("http://127.0.0.1:8000/image/image_model/saveimg/")
          .then((response) => console.log(response))
          .catch((error) => console.log(error))
      })
      .catch(function (error) {
        console.log(error);
      })
    axios
      .post("http://127.0.0.1:8080/crawling/saveimg/", formData, {
        headers: {
          'content-type': 'multipart/form-data'
        }
      })
      .then(function (res) {
        console.log(res);
        axios
          .get("http://127.0.0.1:8080/crawling/saveimg/")
          .then((res) => console.log(res))
          .catch((error) => console.log(error))

      })
      .catch(function (error) {
        console.log(error);
      })
  };
  const postKeyword = async () => {
    let response1 = await axios.post("http://127.0.0.1:8000/image/image_model/");
    return console.log(response1);
  }
  const getKeyword = async () => {
    try {
      let res = await axios.get("http://127.0.0.1:8000/image/image_model/")
      let arr = res.data
      setKeyword(arr[arr.length - 1].title);  //이안에서는 keyword값이 바뀌지 않음 나와서 실행됨.
      let response = await axios.post("http://127.0.0.1:8080/crawling/", {
        "keyword": arr[arr.length - 1].title,
        "hashtag": "hashtag"
      });
      console.log(response.data)
    } catch (error) {
      console.log(error);
      setLoading(false);
    }
  };
  const handleCrawling = async () => {
    try {
      //id를 가져오기 위함
      let res1 = await axios.get(`http://127.0.0.1:8080/crawling/`);
      let arrId = res1.data
      let ori_Id = arrId[arrId.length - 1].id; // 현재 참조 id
      let id = arrId[arrId.length - 1].id;
      for (let i = 0; i < arrId.length-1; i++) {
        if ((arrId[i].keyword === arrId[arrId.length - 1].keyword) && (arrId[i].hashtag !== "hashtag")) {
          id = arrId[i].id; // 해시태그 값들이 있는 id
        }
      }
      const strId = id.toString();
      console.log(strId);
      //여기서 가장 최근 저장된 키워드의 크롤링이 시작되어 hashtag 필드가 수정됨.
      if (ori_Id === id) {
        let res2 = await axios.put(`http://127.0.0.1:8080/crawling/${strId}/`);
        console.log(res2);
        let res3 = await axios.get(`http://127.0.0.1:8080/crawling/`);
        console.log(res3);
        let arrHashtag = res3.data
        console.log(arrHashtag)
        setHashtag(arrHashtag[arrHashtag.length - 1].hashtag);
	setLoading(false);
      }
      else {
        let res4 = await axios.put(`http://127.0.0.1:8080/crawling/${strId}/`);
        console.log(res4);
	let res5 = await axios.get(`http://127.0.0.1:8080/crawling/`);
        console.log(res5);
        let arrHashtag2 = res5.data
        console.log(arrHashtag2)
	setHashtag(arrHashtag2[arrHashtag2.length - 1].hashtag);
	//setHashtag(arrHashtag2["hashtag"]);
	setLoading(false);
      }
    } catch (err) {
      setLoading(false);
      console.log(err);
    }
  };
  return (
    <div>
      {loading ? <Loading /> : null} {/*Loading이 true면 컴포넌트를 띄우고, false면 null(빈 값)처리 하여 컴포넌트 숨김*/}
      <HtagRcmdTemplate
      form={(
        <ImageForm
          onChange={handleInputImage}
          onClick={async () => {
            setLoading(true);
            await postKeyword();
            await getKeyword();
            await handleCrawling();
          }}
        />
      )}
      children={(
        <HtagRcmdList
          hashtag={hashtag}
          checkedList={checkedList}
          setCheckedList={setCheckedList}
          copy={copy}
          setCopy={setCopy}
        />
      )}
      children2={(
        <SelectedHtag
          selectedHtag={checkedList}
          copy={copy}
          setCopy={setCopy}
        />
      )}
    />
    </div>

  )
}


export default Image;
