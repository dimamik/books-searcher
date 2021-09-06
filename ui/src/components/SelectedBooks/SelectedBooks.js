import SingleBookResult from "../SearchPage/SingleBook/SingleBookResult";
import {List, ListItem} from "@material-ui/core";
import styled from "styled-components";
import {StyledItalic} from "../../styles/Styles";


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


    const deleteBook = (book) => {
        //TODO API DOESN'T SUPPORT THIS FUNCTIONALITY

        // let index = selectedBooks.indexOf(book);
        //
        // let arrayTmp = [...selectedBooks];
        // arrayTmp.splice(index, 1)
        //
        // if (index !== -1) {
        //     setSelectedBooks(arrayTmp);
        // }
        // deleteSelectedBook(arrayTmp, book);

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

    return <div
        className='section page'>
        <div
            style={{
                marginTop: '4vh',
            }}
        >
            <StyledH1>Selected books</StyledH1>
        </div>

        <div
            className='scrollable-content'

            style={
                {
                    maxHeight: '85vh',
                    overflowY: 'auto'
                }
            }
        >
            <List style={{marginTop: '2vh', padding: 0}}
            >
                {options}
            </List>
        </div>

        <div
            style={{
                textAlign: 'center',
                margin: '1vh',
                position: 'absolute',
                bottom: '2vh',                 /* adjust this value to move link up or down */
                left: '50%',                   /* center link horizontally */
                transform: 'translateX(-50%)'
            }}
        >
            <StyledItalic>
                Swipe Down <b>There</b> To Get Recommendations
            </StyledItalic>
        </div>


    </div>

}
