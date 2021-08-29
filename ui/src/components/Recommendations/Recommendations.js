import SingleBookResult from "../SearchPage/SingleBook/SingleBookResult";
import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";
import {useEffect, useState} from "react";
import {getRecommendations} from "../../services/RecomService";


const StyledList = styled(ListItem)`
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
`

const StyledH1 = styled.h1`
  font-family: inherit;
  font-weight: bold;
  font-size: x-large;
`

export default function Recommendations() {


    //TODO Update Automatically Recommendations on page load using fullPage prop

    let [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        getRecommendations().then((result) => {
            if (result != null) {
                setRecommendations(result.data);
            } else {
                setRecommendations([]);
            }
        })
    }, recommendations)


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
            <List style={{marginTop: '2vh', padding: 0}}>
                {options}
            </List>
        </div>

    </div>

}
