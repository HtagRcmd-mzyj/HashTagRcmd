import React, {useState} from "react";
import TextForm from "../components/TextForm";
import HtagRcmdList from "../components/HtagRcmdList";
import SelectedHtag from "../components/SelectedHtag";
import HtagRcmdTemplate from "../components/HtagRcmdTemplate";
import axios from "axios";
import Loading from "../components/Loading";
axios.defaults.withCredentials = true;



function Text() {
  const [hashtag, setHashtag] = useState("");
  const [checkedList, setCheckedList] = useState([]);
  const [copy, setCopy] = useState(false);
  const [loading, setLoading] = useState(false);
  const ShowRcmdTopWord = async () => {
    setLoading(()=>true);
    try {
      let res = await axios.post("http://127.0.0.1:80/text/text_model/", {
        "input_text": document.getElementById("input_text").value,
        "hashtag": "none"
      });
      console.log(res);
      //id를 가져오기 위함
      let res2 = await axios.get(`http://127.0.0.1:80/text/text_model`);
      let arrId = res2.data
      let id = arrId[arrId.length - 1].id;
      const strId = id.toString();
      console.log(strId);
      console.log(res2);
      //
      let res3 = await axios.put(`http://127.0.0.1:80/text/text_model/${strId}/`);
      console.log(res3);
      //
      let res4 = await axios.get(`http://127.0.0.1:80/text/text_model`);
      console.log(res4);
      let arrHashtag = res4.data;
      setHashtag(arrHashtag[arrHashtag.length - 1].hashtag);
      console.log(arrHashtag[arrHashtag.length - 1].hashtag);
      setLoading(()=> false);
    } catch (error) {
      console.log(error);
      setLoading(false);
    }

  };
  return (
    <div>
      {loading ? <Loading /> : null}
      <HtagRcmdTemplate
      form={(
        <TextForm
          onClick={ShowRcmdTopWord}
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
  );
}


export default Text;
