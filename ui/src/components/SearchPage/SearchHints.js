import SingleBookHint from "./SingleBook/SingleBookHint";
import {List} from "@material-ui/core";
import {useContext} from "react";
import {selectBookContext} from "../../App";
import {StyledListItem} from "../../styles/Styles";


export default function SearchHints({listOfBooks, searchQuery}) {

    const selectBook = useContext(selectBookContext);

    const options = listOfBooks.map(r => (

        //TODO Change number of hints displayed

        <StyledListItem button key={r._id}
                        style={{
                            borderTop: r._id === listOfBooks[0]._id ?
                                'none' : null,
                            boxShadow: r._id === listOfBooks[listOfBooks.length - 1]._id ?
                                'none' : null,
                        }}
                        onClick={() => {
                            selectBook(r);
                        }}
        >
            <SingleBookHint book={r._source} searchQuery={searchQuery}/>
        </StyledListItem>

    ))

    return <
    >

        <List
            className='scrollable-content'
            style={{
                overflowY: "auto",
                maxHeight: '80vh',
                padding: 0
            }}>
            {options}
        </List>

    </>

}