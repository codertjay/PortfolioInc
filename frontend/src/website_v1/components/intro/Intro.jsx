import React, {useEffect, useRef} from 'react';
import './intro.scss'
import {init} from 'ityped'

function Intro(props) {
    const textRef = useRef();
    useEffect(() => {
        init(textRef.current, {
            showCursor: true,
            strings: ['Developer', 'Designer', 'Content Create'],
            backDelay: 1500,
            backSpeed: 60,
        })
    }, [])

    return (
        <div className={'intro'} id='intro'>
            <div className="left">
                <div className="imgContainer">
                    <img src="assets/man.png" alt=""/>
                </div>

            </div>
            <div className="right">
                <div className="wrapper">
                    <h2>Hi There, I'm</h2>
                    <h1>Afenikhena Favour</h1>
                    <h3>FreeLance <span ref={textRef}> </span></h3>
                </div>
                <a href="#portfolio">
                    <img src="assets/down.png" alt=""/>
                </a>
            </div>

        </div>
    );
}

export default Intro;