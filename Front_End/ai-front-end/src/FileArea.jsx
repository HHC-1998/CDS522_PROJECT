import React from "react";
import "./FileArea.css"

export default class FileArea extends React.Component{
    render(){

        // 接受从父组件传来的数据并解构
        const {fileData} = this.props

        return(
        <div className = "FileAreaDiv"> 

            <h1>Complaint Information Form</h1>
            <p>Date Received : {fileData.dateReceived}</p> 
            <p style={{width:"20%", display:"inline"}}>Source : {fileData.source}</p>
            <p style={{width:"60%", display:"inline"}}># {fileData.hashtag}</p>
            <p>Type : {fileData.type}</p>
            <p>Name of Caller : {fileData.nameOfCaller}</p>
            <p>Contact No. : {fileData.contactNo}</p>
            <p>Slope No. : {fileData.slopeNo}</p>
            <p>Location : {fileData.location}</p>
            <p>Nature of Request : {fileData.natureOfRequest}</p>
            <p>Subject Matter : {fileData.subjectMatter}</p>
            <p>10-day Rule Due Date : {fileData.tenDayRuleDueDate}</p>
            <p>ICC Interim Reply Due Date : {fileData.ICCInterimReplyDueDate}</p>
            <p>ICC Final Reply Due Date : {fileData.ICCFinalReplyDueDate}</p>
            <p>Works Completion Due Date : {fileData.worksCompletionDueDate}</p>
            <p>Fax to Contractor on : {fileData.faxToContractorOn}</p>
            <p>Fax Page(s) 1 + {fileData.faxPages}</p>
            <p>Case Details : {fileData.caseDetails}</p>

        </div>
        )
    }
}