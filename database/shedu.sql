-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2023 a las 07:45:43
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `shedu`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `courses`
--

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL,
  `course` varchar(50) NOT NULL,
  `contraction` varchar(15) NOT NULL,
  `parallel_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `courses`
--

INSERT INTO `courses` (`course_id`, `course`, `contraction`, `parallel_id`, `teacher_id`) VALUES
(1, 'Tercero de Bachillerato', '3º Bach', 5, 2),
(2, 'Tercero de Bachillerato', '3º Bach', 6, 2),
(7, 'Noveno', '9no', 1, 5),
(8, 'Décimo', '10mo', 1, 4),
(9, 'Décimo', '10mo', 2, 10),
(10, 'Noveno', '9no', 2, 3),
(11, 'Segundo de Bachillerato', '2ºBach', 5, 6),
(12, 'Segundo de Bachillerato', '2ºBach', 6, 7),
(13, 'Primero de Bachillerato', '1ºBach', 6, 8),
(14, 'Primero de Bachillerato', '1ºBach', 5, 1),
(15, 'Octavo', '8vo', 1, 13),
(16, 'Octavo', '8vo', 2, 1),
(17, 'Séptimo', '7mo', 2, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `course_subject`
--

CREATE TABLE `course_subject` (
  `course_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `hours` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `course_subject`
--

INSERT INTO `course_subject` (`course_id`, `subject_id`, `hours`) VALUES
(1, 1, 9),
(1, 2, 2),
(1, 3, 7),
(1, 4, 5),
(1, 5, 4),
(1, 6, 3),
(1, 7, 2),
(1, 8, 1),
(2, 1, 8),
(2, 2, 5),
(2, 3, 9),
(2, 5, 6),
(9, 1, 5),
(9, 3, 2),
(9, 4, 5),
(9, 7, 2),
(10, 4, 4),
(11, 8, 1),
(15, 3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `course_subject_teacher`
--

CREATE TABLE `course_subject_teacher` (
  `course_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `hours` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `course_subject_teacher`
--

INSERT INTO `course_subject_teacher` (`course_id`, `subject_id`, `teacher_id`, `hours`) VALUES
(1, 4, 3, 3),
(1, 5, 5, 3),
(1, 6, 4, 2),
(2, 1, 3, 5),
(2, 2, 2, 4),
(2, 3, 5, 4),
(2, 6, 4, 2),
(2, 7, 10, 2),
(2, 8, 2, 2),
(7, 4, 3, 3),
(7, 7, 10, 2),
(8, 3, 13, 3),
(8, 8, 6, 1),
(8, 9, 13, 2),
(9, 9, 5, 4),
(15, 5, 5, 3),
(16, 1, 2, 3),
(16, 6, 4, 3),
(17, 1, 7, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `course_teacher`
--

CREATE TABLE `course_teacher` (
  `course_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genders`
--

CREATE TABLE `genders` (
  `gender_id` int(11) NOT NULL,
  `gender` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `genders`
--

INSERT INTO `genders` (`gender_id`, `gender`) VALUES
(1, 'Masculino'),
(2, 'Femenino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parallels`
--

CREATE TABLE `parallels` (
  `parallel_id` int(11) NOT NULL,
  `parallel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `parallels`
--

INSERT INTO `parallels` (`parallel_id`, `parallel`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(5, 'Técnico en Informática'),
(6, 'Ciencias o loqueros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salutation`
--

CREATE TABLE `salutation` (
  `salutation_id` int(11) NOT NULL,
  `salutation` varchar(25) NOT NULL DEFAULT 'Prof.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `salutation`
--

INSERT INTO `salutation` (`salutation_id`, `salutation`) VALUES
(4, 'Mr.'),
(5, 'Ing.'),
(6, 'Lic.'),
(7, 'Sr.'),
(8, 'Sra.'),
(9, 'Dr.'),
(10, 'Psic.'),
(11, 'Msc.'),
(12, 'Prof.'),
(13, 'Ms.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL,
  `subject` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `subjects`
--

INSERT INTO `subjects` (`subject_id`, `subject`) VALUES
(1, 'Matemáticas'),
(2, 'Lengua y Literatura'),
(3, 'Química'),
(4, 'Física'),
(5, 'Biología'),
(6, 'Historia'),
(7, 'Inglés'),
(8, 'S.T.E.A.M'),
(9, 'Emprendimiento y Gestión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subject_teacher`
--

CREATE TABLE `subject_teacher` (
  `subject_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `teachers`
--

CREATE TABLE `teachers` (
  `teacher_id` int(11) NOT NULL,
  `salutation_id` int(11) DEFAULT NULL,
  `first_name` varchar(25) NOT NULL,
  `second_name` varchar(25) NOT NULL,
  `first_lastname` varchar(25) NOT NULL,
  `second_lastname` varchar(25) NOT NULL,
  `work_hours` int(2) UNSIGNED NOT NULL,
  `gender_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `teachers`
--

INSERT INTO `teachers` (`teacher_id`, `salutation_id`, `first_name`, `second_name`, `first_lastname`, `second_lastname`, `work_hours`, `gender_id`) VALUES
(1, 5, 'Miguel', 'Adrian', 'Gómez', 'Solórzano', 8, 1),
(2, 13, 'Juana', 'Elizabeth', 'Quevedo', 'Caisaguano', 8, 2),
(3, 6, 'José', 'Eduardo', 'Pinargote', 'Velasquez', 8, 1),
(4, 13, 'Laura', 'Ketty', 'Sánchez', 'Salazar', 8, 2),
(5, 5, 'Hugo', 'Michael', ' Moncayo', 'Bermúdez', 8, 1),
(6, 6, 'Israel', 'Josue', 'Chumi', 'Martillo', 8, 1),
(7, 6, 'William', 'Fernando', 'Burgos', 'Ronquillo', 8, 1),
(8, 10, 'Karla', 'Denisse', 'Duarte', 'Mendoza', 8, 2),
(10, 4, 'Ramón', 'Juan', 'Contreras', 'Riofrío', 8, 1),
(11, 11, 'Angela', 'Alexandra', 'Contreras', 'Riofrío', 8, 2),
(12, 6, 'Karen', 'Sara', 'Ramírez', 'Lavayen', 8, 2),
(13, 6, 'César', 'Steven', 'Andrade', 'León', 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `teacher_id` int(11) NOT NULL,
  `user` varchar(15) NOT NULL,
  `password` varbinary(255) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`teacher_id`, `user`, `password`, `admin`) VALUES
(1, 'admin', 0x7363727970743a33323736383a383a312462366d68634a6d59517a4744477a4e74243934656561396535666530303131313932316261626565633761323131623038313564363837343132363862613439643166346463653739653437623338663865646234636232636638633930333965306138366565343561353533663237333063643866366139386439313766313166613639356232646365623166333466, 1),
(2, 'juanaquevedo', 0x7363727970743a33323736383a383a31246b75566850754568533149457a42664b243339396166613837656432373732623839353663623439663631386630363861346239323236656132633835333032636534386138326361613434326165653662623965613332386137376632346533363632383134643933653137353963626233336432623634646234383164346137366138333138396139393066353037, 0),
(3, 'gaussjordan', 0x7363727970743a33323736383a383a3124726433726b4865484379576458327279246237393965306233313161663233613034333037346163643232306538623262623330393439623139396431313530396534353036653732366631636464636338616363373763666431373736616564326361316664623739323238653835626162316261386136653830363438643933386562333866393832396636306366, 0),
(4, 'traka', 0x7363727970743a33323736383a383a312432786c67733530546b7052667133786f243362666664666666353736346138303232356137653633336264383530306238616462643266663966313337343266386439623531666166316566626262396561646366386334313330326261626539353264643234663862636136626431633232366366343261383063653365656265363938643863393039346466643563, 0),
(5, 'profHugo', 0x7363727970743a33323736383a383a312467615775524551394b426b4231705157243831323439633833623938663665616232373438346631323566323962663335623838613461643136393231383165663030666439376333653861646264313462396633316362323065323634366163303033346135323130323066363438376238386538666563333734646466643639626335396263306338646362356264, 0),
(6, 'prof_chumi', 0x7363727970743a33323736383a383a312471463455765a664a303776576e647a47246236626230393036316664303739363831383337373333636533323432343032363431616161353862643938393736623738353863313432346334366333653762333734646238386637316362663561353237323536616330353833616566613532386132326330396131306466356538656161663762366537353161346137, 0),
(7, 'WilliamB', 0x7363727970743a33323736383a383a31246d574544306d626445676465344e7633243935646335383162626130613266306435303961616464646631663138373133633563386565373932353964356433313434656264326664396632363535393765663862653139373331333634306438383634313161653961633938346565653132346437643338323363613366386132383433393235343530306139343064, 1),
(10, 'ramoncito', 0x7363727970743a33323736383a383a31244974794a5442473941585a6a37373644246332353438663235303635386138356436363137346266333238623639623839633164343035633264646338323935636665613138656334396238653066326361363030303239636365663734363330636463396339386561303663313336373139333730643039623163333834623236303333666533663266323631643536, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `paralel_id` (`parallel_id`) USING BTREE;

--
-- Indices de la tabla `course_subject`
--
ALTER TABLE `course_subject`
  ADD PRIMARY KEY (`course_id`,`subject_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `course_id` (`course_id`) USING BTREE;

--
-- Indices de la tabla `course_subject_teacher`
--
ALTER TABLE `course_subject_teacher`
  ADD PRIMARY KEY (`course_id`,`subject_id`),
  ADD KEY `course_subject_teacher_ibfk_2` (`subject_id`),
  ADD KEY `course_subject_teacher_ibfk_3` (`teacher_id`);

--
-- Indices de la tabla `course_teacher`
--
ALTER TABLE `course_teacher`
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indices de la tabla `genders`
--
ALTER TABLE `genders`
  ADD PRIMARY KEY (`gender_id`);

--
-- Indices de la tabla `parallels`
--
ALTER TABLE `parallels`
  ADD PRIMARY KEY (`parallel_id`);

--
-- Indices de la tabla `salutation`
--
ALTER TABLE `salutation`
  ADD PRIMARY KEY (`salutation_id`);

--
-- Indices de la tabla `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`);

--
-- Indices de la tabla `subject_teacher`
--
ALTER TABLE `subject_teacher`
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indices de la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`teacher_id`),
  ADD KEY `salutation_id` (`salutation_id`),
  ADD KEY `gender_id` (`gender_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`teacher_id`) USING BTREE,
  ADD UNIQUE KEY `user` (`user`) USING BTREE;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `courses`
--
ALTER TABLE `courses`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `genders`
--
ALTER TABLE `genders`
  MODIFY `gender_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `parallels`
--
ALTER TABLE `parallels`
  MODIFY `parallel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `salutation`
--
ALTER TABLE `salutation`
  MODIFY `salutation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `teachers`
--
ALTER TABLE `teachers`
  MODIFY `teacher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `courses`
--
ALTER TABLE `courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`parallel_id`) REFERENCES `parallels` (`parallel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `courses_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `course_subject`
--
ALTER TABLE `course_subject`
  ADD CONSTRAINT `course_subject_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `course_subject_teacher`
--
ALTER TABLE `course_subject_teacher`
  ADD CONSTRAINT `course_subject_teacher_ibfk_3` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`),
  ADD CONSTRAINT `course_subject_teacher_ibfk_4` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `course_teacher`
--
ALTER TABLE `course_teacher`
  ADD CONSTRAINT `course_teacher_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`),
  ADD CONSTRAINT `course_teacher_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `subject_teacher`
--
ALTER TABLE `subject_teacher`
  ADD CONSTRAINT `subject_teacher_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`),
  ADD CONSTRAINT `subject_teacher_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`);

--
-- Filtros para la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`salutation_id`) REFERENCES `salutation` (`salutation_id`),
  ADD CONSTRAINT `teachers_ibfk_2` FOREIGN KEY (`gender_id`) REFERENCES `genders` (`gender_id`);

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
