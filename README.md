# Приложение знакомтсв на основе API VK "VKinder"

Алгоритм работы:
При запуске приложение запрашивает ID пользователя, для которого нужно выполнить поиск. Далее нужно ввести условия поиска пользователей, в
случае неправильного ввода приложение сообщает об этом и просит ввести данные заново. В случае отсутствия данных (если пользователь просто
нажал Enter) данные считаются аналогичными данным пользователя, кроме полей возраста (минимальное значение принимается равным 1,
максимальное 90) и пола (в случае неправильного ввода выдаётся ошибка). Условия поиска разделены на более важные (пол, возраст, город) и
менее важные (интересы, книги, музыка). Поиск пользователей выполняется по более приоритетным условиям, затем из них отбираются те, кто
удовлетворяет условиям "побочным". У тех, кто им удовлетворяет, находятся 3 фотографии профиля с наибольшим количеством лайков из 20
последних. Результат записывается в json-файл, где содержатся id пользователя, количество совпадений (которое можно расценивать как 
степень соответствия) и список из 3 id наиболее популярных фотграфий в порядке уменьшения популярности.
