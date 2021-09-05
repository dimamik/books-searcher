import SingleBookResult from "../SearchPage/SingleBook/SingleBookResult";
import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";
import React from "react";
import {StyledButton, StyledDiv} from "../ChooseBook/ChooseBookDialog";
import {deleteCachedUserId} from "../../services/SelectedBooksCacheService";


const StyledList = styled(ListItem)`
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
`

const StyledH1 = styled.h1`
  font-family: inherit;
  font-weight: bold;
  font-size: x-large;
`

export default function Recommendations({recProvider}) {


    //TODO Update Automatically Recommendations on page load using fullPage prop

    let [recommendations, setRecommendations] = recProvider;


    const options = recommendations.map(r => (

        <StyledList button key={r._id}
        >
            <SingleBookResult book={r._source}/>
        </StyledList>


    ))

    return <div className='section'>

        <div
            style={
                {
                    marginTop: '5vh'
                }
            }>
            <StyledH1>Recommended books</StyledH1>
            <List
                className='scrollable-content'
                style={{
                    marginTop: '2vh',
                    padding: 0,
                    maxHeight: '80vh',
                    overflowY: 'auto'

                }}>
                {options}
            </List>
        </div>
        <StyledDiv>
            <StyledButton
                onClick={deleteCachedUserId}
                style={{
                    position: 'absolute',
                    bottom: '2vh',                 /* adjust this value to move link up or down */
                    left: '50%',                   /* center link horizontally */
                    transform: 'translateX(-50%)'
                }}
                href='#welcomePage'
            >
                Clear All
            </ StyledButton>
        </StyledDiv>
    </div>

}
