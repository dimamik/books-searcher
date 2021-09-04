import {StyledHeader, StyledItalic, StyledNormal} from "../../../styles/Styles";
import {searchBookInGoogle} from "../../../services/SearchService";


export default function SingleBookResult({book}) {

    const findBookGoogle = () => {
        console.log(book);
        searchBookInGoogle(book.book_name);
    }

    return <div
        onClick={findBookGoogle}
    >
        <StyledHeader>

            <span>{book.book_name}</span>

        </StyledHeader>

        <StyledHeader style={{
            position: 'absolute', right: '2vh'
        }}>
            <span>{book.book_points}</span>
        </StyledHeader>
        <StyledItalic style={{
            marginLeft: '3vh',
            marginRight: '3vh'
        }}>

            <span>{book.book_author}</span>
        </StyledItalic>
        <StyledNormal
            style={{
                marginLeft: '1vh',
                overflow: 'clip'
            }}
        >
            <span>{book.book_description}</span>

        </StyledNormal>

    </div>

}