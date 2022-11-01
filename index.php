<?php








class Genre
{
	public $genreName;

	

}


class GenreByNumberOfPages extends Genre
{
	public $volume;
	

}

class GenreByForm extends Genre
{
	

}


class GenreByContent extends Genre
{
	public $description;
	

}



class Story extends GenreByNumberOfPages
{
	public $genreName = "Story";


}


class Novel extends GenreByNumberOfPages
{
	public $genreName = "Novel";
	
}


class Narrative extends GenreByNumberOfPages
{
	public $genreName = "Narrative";
	
}




class Prose extends GenreByForm
{
	public $genreName = "Prose";
	
}

class Verse extends GenreByForm
{
	public $genreName = "Verse";
	
}





class Fantastic extends GenreByContent
{
	public $genreName = "Fantastic";
	
}


class Detective extends GenreByContent
{
	public $genreName = "Detective";
	
}

class Professional extends GenreByContent
{
	public $genreName = "Professional";
	
}


include_once "library/book.php";
include_once "library/BookService.php";


$book1 = new Book("asd", "asd", [new Story(), new Verse()]);
$book2 = new Book("asdfvd", "asfvd", [new Story(), new Fantastic()]);
$book3 = new Book("assssd", "assssd", [new Novel(), new Detective()]);
 






$filter = new BookService();
$filter->filterBookByGenre([$book1, $book2, $book3],  Novel);


?>








