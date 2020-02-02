import React, { useState } from 'react';
import axios from 'axios'
import './App.css';
import './tailwind_styles.css'
import 'antd/dist/antd.css';

import {Upload, message, Button, Icon, Switch} from 'antd'

function App() {

  const [selectedFile, setSelectedFile] = useState()
  const [uploadedFile, setUploadedFile] = useState()
  const [displayImage, setDisplayImage] = useState(false)
  const [darkMode, setDarkMode] = useState(false)

  const props = {
    name: 'file',
    action: 'https://www.mocky.io/v2/5cc8019d300000980a055e76',
    headers: {
      authorization: 'authorization-text',
    },

    onChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };


  function handleFileSelect (info) {
    console.log(info.file.originFileObj)
    //setSelectedFile(event.target.files[0])
  }

  function handleFileUpload (event) {
    const fd = new FormData ()

    fd.append('image', selectedFile)
    axios.post('http://localhost:5000/upload_file', fd, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(res => {
      const {fileName, filePath} = res.data 
      setUploadedFile({fileName, filePath})
    })
    .catch(error => console.log(error))
    console.log(selectedFile)
  }

  function onSwitchChange() {
    setDarkMode(!darkMode)
  }

  return (
    <>
      <h1 className={darkMode ? "text-4xl sticky self-center font-bold py-2 pl-64 shadow-lg bg-gray-800 text-white mb-0" :"mb-0 text-4xl sticky self-center font-bold py-2 pl-64 shadow-lg"}>ScaleRes.</h1>
      <div className={darkMode ? "bg-gray-700 w-screen h-full absolute pt-1/4" : "pt-1/4 w-screen h-screen absolute"}>
        <div className="px-64 pt-1/2">
          <Switch defaultChecked={false} onChange={onSwitchChange}/>
          <p className={darkMode ? "text-base mt-4 text-white" : "text-base pt-4"}>Increasing the resolution of a small or blurry image has been an exciting area of machine 
          learning research over the last few years as its potential in different industries is being explored, 
          from medical imaging to self-driving cars.<br/><br/>Enter a blurry image you'd like to scale up. Our MegaSuperAdvanced™ 
          Algorithms will then increase the resolution of your image using [insert buzzword here]</p>

          <Upload {...props} onChange={handleFileSelect}>
            <Button>
              <Icon type="upload" /> Click to Upload
            </Button>
          </Upload>
          <Button type="primary" className="mt-3" onClick={handleFileUpload}>Upload</Button>
        </div>

        <div className="mt-10 flex justify-between px-64 w-full">
          <div className="text-left"> 
            <h2 className={displayImage ? "text-lg" : "text-lg invisible"}>Original</h2>
            <img className={displayImage ? "" : "invisible"} src=".../static/uploads/original.png"/>
          </div>
          <div className="text-right">
            <h2 className={displayImage ? "text-lg" : "text-lg invisible"}>SuperSized</h2>
            <img className={displayImage ? "" : "invisible"} src=".../static/uploads/enlarged.png"/>
          </div>
        </div>
      </div>
    </>
  );
}

export default App
