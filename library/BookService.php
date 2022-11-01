<?php


class BookService
{
	public function filterBookByGenre($Books, $genres){
		var_dump($book->genres);
		var_dump($genre);
		foreach ($Books as $book) {
			foreach ($book->genres as $genre ){
				if($genre instanceof $genres){
					var_dump($book);
				}
			}
			
		}
		
	}
}


?>