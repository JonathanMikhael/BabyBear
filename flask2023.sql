-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 30, 2023 at 08:14 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask2023`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `kategori` varchar(25) NOT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `nama_produk` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `harga_jual` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `kategori`, `gambar`, `nama_produk`, `deskripsi`, `harga_jual`) VALUES
(6, 'Pacifier', 'paci1.png', 'Night Glow Baby Blue Pacifier', 'Pacifier', 15000),
(7, 'Pacifier', 'paci2.png', 'Blush Pacifier', 'Pacifier', 17000),
(8, 'Pacifier', 'paci3.png', 'White Pacifier', 'Pacifier', 20000),
(9, 'Pacifier', 'paci4.png', 'Vanilla Pacifier', 'Pacifier', 17000),
(10, 'BabyRides', 'babybugzz.png', 'Babybuggz Sandstone', 'BabyRides', 35000),
(11, 'BabyRides', 'doona.png', 'Doona Grey Hound', 'BabyRides', 32000),
(12, 'BabyRides', 'likitrike.png', 'Liki Trike Gold', 'BabyRides', 37000),
(13, 'BabyRides', 'highrider.png', 'High Rider Brown', 'BabyRides', 40000),
(14, 'Clothings', 'daisy.png', 'Daisy Pattern Tracksuit Grey', 'Clothings', 25000),
(15, 'Clothings', 'dino.png', 'Dinosaur Belge Romper', 'Clothings', 30000),
(16, 'Clothings', 'florence.png', 'Florence Bunny Coat', 'Clothings', 32000),
(17, 'Clothings', 'happyromper.png', 'Happy Romper', 'Clothings', 27000),
(18, 'Clothings', 'lit.jpeg', 'Little Love Romper Sage', 'Clothings', 38000),
(19, 'Clothings', 'poppyfloral.png', 'Poppy Floral', 'Clothings', 40000),
(20, 'Clothings', 'teddy.png', 'Teddy Bear Puffer Coat Brown', 'Clothings', 42000),
(21, 'Clothings', 'archie.png', 'Archie Fleece Coat Brown', 'Clothings', 42000);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `namalengkap` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`namalengkap`, `email`, `username`, `password`) VALUES
('Abdi', 'abdi123@gmail.com', 'a', 'A'),
('Abdi', 'abdi@gmail.com', 'abdi', 'abdi123'),
('B', 'b@gmail.com', 'b', 'b'),
('Bhustomy Hakim', 'bhust@gmail.com', 'bhustomy', '12345'),
('c', 'c@gmail.com', 'c', 'c'),
('d', 'd@gmail.com', 'd', 'd'),
('Sisilia Petrisa', 'silpetrisa@gmail.com', 'sisiliaptrsa', 'lunableue');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
