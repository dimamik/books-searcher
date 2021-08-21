import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";
import SingleBookResult from "./SingleBook/SingleBookResult";
import {useContext} from "react";
import {selectBookContext} from "../../App";

const StyledList = styled(ListItem)`
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;

`


const SearchResults = ({listOfBooks}) => {

    const selectBook = useContext(selectBookContext);

    const options = listOfBooks.map(r => (


        <StyledList button key={r._id}
                    onClick={() => {
                        selectBook(r);
                    }}
        >
            <SingleBookResult book={r._source}/>
        </StyledList>


    ))


    return <>
        <List style={{marginTop: '2vh', padding: 0}}>
            {options}
        </List>
    </>

}

export default SearchResults;