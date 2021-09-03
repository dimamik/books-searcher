import SingleBookResult from "../SearchPage/SingleBook/SingleBookResult";
import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";
import {useState} from "react";
import {deleteSelectedBook} from "../../services/SelectedBooksCacheService";
import {getUserFavourite} from "../../services/RecomService";


const StyledList = styled(ListItem)`
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;

`

const StyledH1 = styled.h1`
  font-family: inherit;
  font-weight: bold;
  font-size: x-large;
`

export default function SelectedBooks({booksReadProvider}) {

    // TODO Crop Text and add ... if not fitted in visible area

    let [selectedBooks, setSelectedBooks] = booksReadProvider;


    useState(() => {
        // getUserFavourite().then(
        //     (result) => {
        //         if (result == null) {
        //             setSelectedBooks([]);
        //         } else {
        //             setSelectedBooks(result.data);
        //         }
        //
        //     }
        // )

    })

    const deleteBook = (book) => {
        let index = selectedBooks.indexOf(book);

        let arrayTmp = [...selectedBooks];
        arrayTmp.splice(index, 1)

        if (index !== -1) {
            setSelectedBooks(arrayTmp);
        }
        deleteSelectedBook(arrayTmp, book);

    }


    const options = selectedBooks?.map(r => (


        <StyledList
            style={{
                paddingBottom: '1vh'
            }}
            button key={r._id} onClick={() => deleteBook(r)}
        >
            <SingleBookResult book={r._source}

            />
        </StyledList>


    ))

    return <div className='section'>

        <div
            style={
                {
                    marginTop: '5vh',
                }
            }
        >
            <StyledH1>Selected books</StyledH1>
            Select a book to remove
            <List style={{marginTop: '2vh', padding: 0}}>
                {options}
            </List>
        </div>

    </div>

}
