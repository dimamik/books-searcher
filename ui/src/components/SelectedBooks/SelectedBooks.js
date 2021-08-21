import SingleBookResult from "../SearchPage/SingleBook/SingleBookResult";
import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";


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

    //TODO Write selected books to browser cache!

    let [selectedBooks, setSelectedBooks] = booksReadProvider;


    const deleteBook = (book) => {
        let index = selectedBooks.indexOf(book);

        console.log(index);
        let arrayTmp = [...selectedBooks];
        arrayTmp.splice(index, 1)


        if (index !== -1) {
            setSelectedBooks(arrayTmp);
        }
    }


    const options = selectedBooks.map(r => (


        <StyledList button key={r._id} onClick={() => deleteBook(r)}
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
            <StyledH1>Selected books</StyledH1>
            Select a book to remove
            <List style={{marginTop: '2vh', padding: 0}}>
                {options}
            </List>
        </div>

    </div>

}
