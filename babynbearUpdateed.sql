-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 08, 2024 at 06:50 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `babynbear`
--

-- --------------------------------------------------------

--
-- Table structure for table `orderData`
--

CREATE TABLE `orderData` (
  `idOrder` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `idProduct` int(11) NOT NULL,
  `qtyProduct` int(11) NOT NULL,
  `totalHarga` int(10) NOT NULL,
  `statusDelivery` varchar(50) NOT NULL,
  `CREATED_AT` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderData`
--

INSERT INTO `orderData` (`idOrder`, `username`, `idProduct`, `qtyProduct`, `totalHarga`, `statusDelivery`, `CREATED_AT`) VALUES
(1, 'b', 10, 1, 35000, 'Delivered', '2024-01-05'),
(2, 'b', 11, 1, 32000, 'Delivered', '2024-01-05'),
(3, 'c', 6, 2, 30000, 'Delivered', '2024-01-08'),
(4, 'abdi', 6, 1, 15000, 'Delivered', '2024-01-08'),
(5, 'abdi', 7, 1, 17000, 'Delivered', '2024-01-08'),
(6, 'abdi', 6, 1, 15000, 'Delivered', '2024-01-08'),
(7, 'abdi', 7, 1, 17000, 'Delivered', '2024-01-08'),
(8, 'abdi', 9, 3, 51000, 'Delivered', '2024-01-08');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `idProduct` int(11) NOT NULL,
  `kategori` varchar(25) NOT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `nama_produk` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `harga_jual` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`idProduct`, `kategori`, `gambar`, `nama_produk`, `deskripsi`, `harga_jual`) VALUES
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
  `password` varchar(30) NOT NULL,
  `userRole` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`namalengkap`, `email`, `username`, `password`, `userRole`) VALUES
('Abdi', 'abdi123@gmail.com', 'a', 'A', 'user'),
('Abdi', 'abdi@gmail.com', 'abdi', 'abdi123', 'user'),
('B', 'jonathan.anthony886@gmail.com', 'b', 'b', 'admin'),
('Bhustomy Hakim', 'asdasdasxasxasx@gmail.com', 'bhustomy', '12345', 'user'),
('c', 'c@gmail.com', 'c', 'c', 'admin'),
('d', 'd@gmail.com', 'd', 'd', 'admin'),
('Sisilia Petrisa', 'silpetrisa@gmail.com', 'sisiliaptrsa', 'lunableue', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orderData`
--
ALTER TABLE `orderData`
  ADD PRIMARY KEY (`idOrder`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`idProduct`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orderData`
--
ALTER TABLE `orderData`
  MODIFY `idOrder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `idProduct` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
