import React, {useEffect, useState} from 'react';
import './portfolio.scss'
import PortfolioList from "../portfolioList/PortfolioList";
import '../../data';
import {contentPortfolio, designPortfolio, featuredPortfolio, mobilePortfolio, webPortfolio} from "../../data";

function Portfolio() {
    const [selected, setSelected] = useState('featured');
    const [data, setData] = useState([]);

    const list = [
        {
            id: 'featured',
            title: 'Featured'
        }, {
            id: 'web',
            title: 'Web App'
        }, {
            id: 'mobile',
            title: 'Mobile App'
        }, {
            id: 'design',
            title: 'Design'
        }, {
            id: 'content',
            title: 'Branding'
        },
    ]
    useEffect(() => {
        switch (selected) {
            case 'featured':
                setData((featuredPortfolio))
                break;
            case 'web':
                setData((webPortfolio))
                break;
            case 'mobile':
                setData((mobilePortfolio))
                break;
            case 'design':
                setData((designPortfolio))
                break;
            case 'content':
                setData((contentPortfolio))
                break;
        }
    }, [selected]);


    return (
        <div className={'portfolio'} id={'portfolio'}>
            <h1>Portfolio</h1>
            <ul>
                {list.map((item) => (
                    <PortfolioList title={item.title} id={item.id}
                                   active={selected === item.id}
                                   setSelected={setSelected}/>
                ))}
            </ul>
            <div className="container">
                {
                    data.map((item, id) => (
                        <div className="item">
                            <img
                                src={item.img}
                                alt=""/>
                            <h3>{item.title}</h3>
                        </div>
                    ))
                }
            </div>
        </div>
    );
}

export default Portfolio;