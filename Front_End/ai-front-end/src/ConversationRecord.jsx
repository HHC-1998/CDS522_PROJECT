import React from "react";
import "./ConversationRecord.css"

export default class ConversationRecord extends React.Component{
    render(){

        // 接受从父组件传来的列表信息
        const dialog = this.props.dialogData

        return(
            <div className="Record">
                {dialog.map((text, index) => {
                    return <p className="QandA" key={index}> {text} </p>
                })}
            </div>
        )
    }
}