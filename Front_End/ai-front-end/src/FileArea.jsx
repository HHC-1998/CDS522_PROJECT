import React from "react";
import "./FileArea.css"

export default class FileArea extends React.Component{
    render(){
        return(
        <div className = "FileAreaDiv"> 

            <h1>Complaint Information Form</h1>
            <p>Date Received :</p> 
            <p style={{width:"20%", display:"inline"}}>Source :</p>
            <p style={{width:"60%", display:"inline"}}># </p>
            <p>Type :</p>
            <p>Name of Caller :</p>
            <p>Contact No. :</p>
            <p>Slope No. :</p>
            <p>Location :</p>
            <p>Nature of Request :</p>
            <p>Subject Matter :</p>
            <p>10-day Rule Due Date :</p>
            <p>ICC Interim Reply Due Date :</p>
            <p>ICC Final Reply Due Date :</p>
            <p>Works Completion Due Date :</p>
            <p>Fax to Contractor on :</p>
            <p>Fax Page(s) 1 + </p>
            <p>Case Details :</p>

        </div>
        )
    }
}