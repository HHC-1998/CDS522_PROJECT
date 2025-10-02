import React from "react";
import "./MainPage.css"
import NavigationBar from "./NavigationBar";
import ConversationArea from "./ConversationArea";

export default class MainPage extends React.Component{
    render(){
        return( 
        <div className="MainPageDiv">
            <NavigationBar></NavigationBar>
            <ConversationArea></ConversationArea>
        </div> 
    )
    }
}