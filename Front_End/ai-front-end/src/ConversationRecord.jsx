import React from "react";
import "./ConversationRecord.css"

export default class ConversationRecord extends React.Component{

    constructor(){
        super();
        this.state={
            testList : ["test1", "test2", "test3", "test4", "test5", "test6", "test17", "test8", "test1", "test2", "test3", "test4", "test5", "test6", "test17"]
        }
    }


    render(){
        return(
            <div className="Record">

                {this.state.testList.map((test, index) => {
                    return <div key={index}> {test} </div>
                })}

            </div>
        )
    }
}