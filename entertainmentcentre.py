import media
import fresh_tomatoes
import webbrowser

allah = media.Song("Allah Ho",
                     "MTV Coke Studio",
                     "http://mtvstat.in.com/252c68bdb46aff808e087ba32cd7c30f_ls_xl.jpg",
                     "https://www.youtube.com/watch?v=Pt0nqbSJiEE")

madari = media.Song("Madari",
                     "MTV Coke Studio",
                     "http://mtvstat.in.com/02bfb81bdeead583f03f38a65a8358ba_ls_xl.jpg",
                     "https://www.youtube.com/watch?v=LRnbNpTUpTo")

bad = media.Song("Badtameez Dil",
                     "Yeh Jawaani Yeh Deewani",
                     "http://media2.intoday.in/indiatoday/images/stories/badtameez-dil_350_040913113720.jpg",
                     "https://www.youtube.com/watch?v=8_ixcsWqC8c")

guns = media.Song("21 Guns",
                     "Green Day",
                     "http://fc08.deviantart.net/fs47/f/2009/173/b/2/21_Guns___2_by_jusso11.jpg",
                     "https://www.youtube.com/watch?v=r00ikilDxW4")

songs=[allah,madari,bad,guns]
fresh_tomatoes.open_movies_page(songs)



