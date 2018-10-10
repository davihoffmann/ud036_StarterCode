# -*- coding: cp1252 -*-
import fresh_tomatoes
import media


# criando as instacias da classe Movie, onde é passado por parâmetro o título, link do poster e link do trailer no youtube
batman_vs_superman = media.Movie("Batman v Superman: Dawn of Justice",
                                 "https://upload.wikimedia.org/wikipedia/pt/" +
                                 "thumb/1/13/Batman_v_Superman_-_Poster_cine" +
                                 "ma.jpg/250px-Batman_v_Superman_-_Poster_ci" +
                                 "nema.jpg",
                                 "https://www.youtube.com/watch?v=IHDgrNxO-5I")

vingadores = media.Movie("Vingadores: Guerra Infinita",
                         "http://br.web.img3.acsta.net/c_215_290/pictures/18" +
                         "/03/16/15/08/2019826.jpg",
                         "https://www.youtube.com/watch?v=t_ULBP6V9bg")

furia_de_titans = media.Movie("Clash of the Titans",
                              "https://upload.wikimedia.org/wikipedia/pt/" +
                              "thumb/f/f9/Clash_of_the_Titans_P%C3%B4ster." +
                              "jpg/220px-Clash_of_the_Titans_P%C3%B4ster.jpg",
                              "https://www.youtube.com/watch?v=VxyNL1IJkoA")

# Criando um array e adicionando as instancias criadas para a lista de filmes
movies = [batman_vs_superman, vingadores, furia_de_titans]

# passando os filmes para a função, onde será gerado o html da página, a função geradora da pagina, recebe um array de instacias da classe Movie
fresh_tomatoes.open_movies_page(movies)
