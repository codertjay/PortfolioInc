import './topbar.scss'
import {Mail, Person} from "@mui/icons-material";

function Topbar({menuOpen, setMenuOpen}) {
    return (
        <div className={'topbar ' + (menuOpen && 'active')}>
            <div className="wrapper">
                <div className="left">
                    <a href="#intro" className={'logo'}>Coderjay.</a>
                    <div className="itemContainer">
                        <Person className={'icon'}/>
                        <span>+44 924 12 74</span>
                    </div>
                    <div className="itemContainer">
                        <Mail className={'icon'}/>
                        <span>codertjay@gmail.com</span>
                    </div>
                </div>
                <div className="right">
                    <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
                        <span className="line1"></span>
                        <span className="line2"></span>
                        <span className="line3"></span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Topbar;