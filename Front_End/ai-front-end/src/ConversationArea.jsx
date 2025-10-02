// 单文件传输以完善，多文件传输尚未完善

import React from "react";
import "./ConversationArea.css";
import FileArea from "./FileArea";
import ConversationRecord from "./ConversationRecord"

export default class ConversationArea extends React.Component{

    userQuestion = ""
    isDisabled = false

    // 构造函数
    constructor(){
        super()
        this.state = {
            userAsk : "",
            fileInformation : [],
            fileName : [],
            receivedData : []
        }
    }

    // 输入文本
    askOnChange = (event) => { 
        this.setState({
            userAsk : event.target.value
        }, () => { 
            console.log(this.state.userAsk)
        }) 
    }

    // 添加文件
    addFile = (event) => { 
        event.preventDefault()
        event.stopPropagation()
        // 文件
        const file = event.dataTransfer.files[0]
        // 文件名
        const fileName = event.dataTransfer.files[0].name 
        // 判断是否是PDF或者TXT
        if(fileName.slice(-4) === ".pdf" || fileName.slice(-4) === ".txt"){
            this.setState({
                fileInformation : file, // 添加文件
                fileName : fileName     // 添加文件名
            })
        } else {
            alert("ONLY TXT AND PDF") // 必须是PDF或者TXT
        }
    }

    // 删除文件
    deletFile = (event) => {
        event.preventDefault()
        event.stopPropagation()
        this.setState({
            fileInformation : [],
            fileName : []
        })
    }

    // 提交表单
    submitQuestion = (event) => {
        event.preventDefault()
        event.stopPropagation()
    }

    // 点击发送
    userSend = (event) => {
        event.preventDefault()
        event.stopPropagation()

        // 判断当下是否有文件要上传（上传文件优先于咨询问题）
        if(this.state.fileInformation.length !== 0){
            // 判断文件类型
            if(this.state.fileInformation.name.slice(-4) === ".txt"){ // TXT文件
                this.fileSender("filetxt")
            } else {
                if(this.state.fileInformation.name.slice(0, 3) === "ASD"){ // PDF文件TMO类型
                    this.fileSender("filetmo")
                } else if(0) {

                } else {
                    alert("INPUT CORRECT FILE")
                }
            }
            this.setState({
                fileInformation : [],
                fileName : []
            })
        } 
        // 发送用户想咨询的问题
        else {
            this.userQuestion = this.state.userAsk
            console.log("User ask: " + this.userQuestion)
            fetch('http://localhost:8000/aitalk?question=' + this.userQuestion, 
            {
                method: 'Get',
                headers: { 'Content-Type': 'application/json' }
            })
            .then(res => res.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.log(error);
            })
        }
    }

    fileSender = (str) => {
        // 将传入的文件封装起来以便于传输
        const formData = new FormData()
        formData.append("File", this.state.fileInformation)
        // 传输txt文件
        fetch('http://localhost:8000/' + str, 
                {
                    method: 'POST',
                    body : formData
                })
                .then(res => res.json())
                .then(data => {
                    this.setState({
                        receivedData : data
                    }, () => {
                        console.log(this.state.receivedData);
                    })
                })
                .catch(error => {console.log(error);})
    }

    render(){
        return(
        <div className="ConversationAreaDiv"> {/*对话框所在容器*/}

            <FileArea></FileArea>
            <ConversationRecord></ConversationRecord>

            <div className="TextAndSend"> {/*输入框与发送按钮表单所在容器*/}
                <form onSubmit={this.submitQuestion}> {/*表单*/}

                    {this.state.fileInformation && <p className="FileName"
                    onClick={this.deletFile}> FILE(Click To Delet): {this.state.fileInformation.name} </p>} {/*用于显示文件名*/}

                    <input className="ConversationInput" 
                    type="text" 
                    placeholder="You can ask anything..." 
                    value={this.state.userAsk} 
                    onChange={this.askOnChange} 
                    onDrop={this.addFile}></input> {/*输入框*/}
                    
                    <button className="ConversationSend" 
                    onClick={this.userSend} 
                    disabled={this.isDisabled}>SEND</button> {/*发送按钮*/}
                </form>
            </div>

        </div>
        )
    }
}