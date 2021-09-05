import React from "react";
import {StyledH1, ZoomedInDiv} from "../../styles/Styles";

export default class WelcomePage extends React.Component {
    render() {
        return (
            <div className='section'>
                <ZoomedInDiv
                >
                    <StyledH1
                        style={{width: '90%'}}
                    >Welcome in Books Recommendations Engine <br/>
                        Please, scroll down to select books you like <br/>
                        And scroll again to get recommendations
                    </StyledH1>
                </ZoomedInDiv>
            </div>

        );
    }
}
