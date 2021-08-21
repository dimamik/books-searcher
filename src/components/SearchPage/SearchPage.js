import SearchField from "./SearchField";
import SearchHints from "./SearchHints";
import {useState} from "react";
import {Box, Grid} from "@material-ui/core";
import SearchResults from "./SearchResults";
import {StyledPaper} from "../../styles/Styles";
import {serviceSearchAPI, serviceSearchAsYouType} from "../../services/SearchService";


export default function SearchPage() {

    let [isTriggered, setIsTriggered] = useState(false);
    let [searchQuery, setSearchQuery] = useState("");
    let [listOfBooks, setListOfBooks] = useState([])
    let [showSearchResults, setShowSearchResults] = useState(false);


    // TODO Place this calls inside functions below
    const searchAPI = (query) => {
        serviceSearchAPI(query).then(
            (res) => setListOfBooks(res)
        )
        // TODO Delete Temp value
        // setListOfBooks(listOfBooksTemp)

    }

    const searchAsYouTypeAPI = (query) => {

        serviceSearchAsYouType(query).then(
            (res) => setListOfBooks(res)
        );
        // TODO Delete Temp value
        // setListOfBooks(listOfBooksTemp)
    }


    const checkQuery = (query) => {
        if (query === "") {
            setListOfBooks([]);
            setSearchQuery(query);
            return null;
        }
        query = query.replaceAll("/", "");
        return query;
    }

    // TODO Compose handlers

    const handleSearchAsYouType = (query) => {
        if ((query = checkQuery(query))) {
            console.log(query)
            setSearchQuery(query);
            setShowSearchResults(false);
            searchAsYouTypeAPI(query);
        }
    }
    const handleSearchButton = (query) => {
        if ((query = checkQuery(query))) {
            setSearchQuery(query);
            setShowSearchResults(true);
            searchAPI(query);
        }
    }

    const triggerSearchBar = () => {
        if (isTriggered && searchQuery.length !== 0) {
            return;
        }
        if (isTriggered) {
            setListOfBooks([]);
        }
        setIsTriggered(!isTriggered);
    }

    return <div
        className="section">
        <Box
            style={{
                marginTop: !isTriggered ? '35vh' : '8vh',
                transition: 'all 0.35s ease-out'
            }}>
            <Grid
                container
                direction="row"
                justifyContent="center"
                alignItems="center"
            >
                <Grid item xs={11} md={8} lg={6}>

                    <StyledPaper component="form"
                                 elevation={12}
                                 style={{
                                     borderRadius: listOfBooks.length === 0 ? 50 : 30
                                 }}
                    >
                        <SearchField
                            handleSearchAsYouType={handleSearchAsYouType}
                            triggerSearchBar={triggerSearchBar}
                            handleSearchButton={handleSearchButton}
                        />

                        {
                            !showSearchResults &&
                            <SearchHints
                                listOfBooks={listOfBooks} searchQuery={searchQuery}
                            />
                        }

                    </StyledPaper>
                </Grid>
            </Grid>

            <Grid
                container
                direction="row"
                justifyContent="center"
                alignItems="center"
            >
                {
                    showSearchResults &&
                    <Grid item xs={11} md={8} lg={6}>

                        <StyledPaper
                            style={{
                                borderRadius: 10,
                                marginTop: '2vh',
                                overflow: 'scroll',
                                height: '80vh'
                            }}
                            className='scrollable-content'
                            elevation={5}
                        >
                            <SearchResults listOfBooks={listOfBooks}/>

                        </StyledPaper>

                    </Grid>
                }
            </Grid>
        </Box>
    </div>
}
