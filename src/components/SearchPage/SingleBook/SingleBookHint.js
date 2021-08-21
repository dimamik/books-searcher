import {StyledHeader, StyledItalic} from "../../../styles/Styles";


function getHighlightedText(text, highlight) {
    // Split on highlight term and include term into parts, ignore case
    const parts = text.split(new RegExp(`(${highlight})`, 'gi'));
    return <span> {parts.map((part, i) =>
        <span key={i} style={part.toLowerCase() === highlight.toLowerCase() ? {color: 'blue'} : {}}>
            {part}
        </span>)
    } </span>;
}

export default function SingleBookHint({book, searchQuery}) {

    return <div style={{textOverflow: 'hidden'}}>
        <StyledHeader>
            <span>{getHighlightedText(book.book_name, searchQuery)}</span>
            <StyledItalic style={{
                marginLeft: '3vh',
            }}>{getHighlightedText(book.book_author, searchQuery)}</StyledItalic>
        </StyledHeader>
    </div>

}