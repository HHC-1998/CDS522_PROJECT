import React from "react";
import "./ConversationRecord.css"

export default class ConversationRecord extends React.Component{

    constructor(){
        super();
        this.state={
            textList : []
        }
    }


    render(){
        return(
            <div className="Record">

                {this.state.textList.map((text, index) => {
                    return <div key={index}> {text} </div>
                })}

            </div>
        )
    }
}