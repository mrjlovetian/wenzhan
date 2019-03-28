# -*- coding: utf-8 -*-
import scrapy
import json
import pymysql
import datetime


class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    offsize = 0
    alldays = ['20120523', '20120524', '20120525', '20120526', '20120527', '20120528', '20120529', '20120530', '20120531', '20120601', '20120602', '20120603', '20120604', '20120605', '20120606', '20120607', '20120608', '20120609', '20120610', '20120611', '20120612', '20120613', '20120614', '20120615', '20120616', '20120617', '20120618', '20120619', '20120620', '20120621', '20120622', '20120623', '20120624', '20120625', '20120626', '20120627', '20120628', '20120629', '20120630', '20120701', '20120702', '20120703', '20120704', '20120705', '20120706', '20120707', '20120708', '20120709', '20120710', '20120711', '20120712', '20120713', '20120714', '20120715', '20120716', '20120717', '20120718', '20120719', '20120720', '20120721', '20120722', '20120723', '20120724', '20120725', '20120726', '20120727', '20120728', '20120729', '20120730', '20120731', '20120801', '20120802', '20120803', '20120804', '20120805', '20120806', '20120807', '20120808', '20120809', '20120810', '20120811', '20120812', '20120813', '20120814', '20120815', '20120816', '20120817', '20120818', '20120819', '20120820', '20120821', '20120822', '20120823', '20120824', '20120825', '20120826', '20120827', '20120828', '20120829', '20120830', '20120831', '20120901', '20120902', '20120903', '20120904', '20120905', '20120906', '20120907', '20120908', '20120909', '20120910', '20120911', '20120912', '20120913', '20120914', '20120915', '20120916', '20120917', '20120918', '20120919', '20120920', '20120921', '20120922', '20120923', '20120924', '20120925', '20120926', '20120927', '20120928', '20120929', '20120930', '20121001', '20121002', '20121003', '20121004', '20121005', '20121006', '20121007', '20121008', '20121009', '20121010', '20121011', '20121012', '20121013', '20121014', '20121015', '20121016', '20121017', '20121018', '20121019', '20121020', '20121021', '20121022', '20121023', '20121024', '20121025', '20121026', '20121027', '20121028', '20121029', '20121030', '20121031', '20121101', '20121102', '20121103', '20121104', '20121105', '20121106', '20121107', '20121108', '20121109', '20121110', '20121111', '20121112', '20121113', '20121114', '20121115', '20121116', '20121117', '20121118', '20121119', '20121120', '20121121', '20121122', '20121123', '20121124', '20121125', '20121126', '20121127', '20121128', '20121129', '20121130', '20121201', '20121202', '20121203', '20121204', '20121205', '20121206', '20121207', '20121208', '20121209', '20121210', '20121211', '20121212', '20121213', '20121214', '20121215', '20121216', '20121217', '20121218', '20121219', '20121220', '20121221', '20121222', '20121223', '20121224', '20121225', '20121226', '20121227', '20121228', '20121229', '20121230', '20121231', '20130101', '20130102', '20130103', '20130104', '20130105', '20130106', '20130107', '20130108', '20130109', '20130110', '20130111', '20130112', '20130113', '20130114', '20130115', '20130116', '20130117', '20130118', '20130119', '20130120', '20130121', '20130122', '20130123', '20130124', '20130125', '20130126', '20130127', '20130128', '20130129', '20130130', '20130131', '20130201', '20130202', '20130203', '20130204', '20130205', '20130206', '20130207', '20130208', '20130209', '20130210', '20130211', '20130212', '20130213', '20130214', '20130215', '20130216', '20130217', '20130218', '20130219', '20130220', '20130221', '20130222', '20130223', '20130224', '20130225', '20130226', '20130227', '20130228', '20130301', '20130302', '20130303', '20130304', '20130305', '20130306', '20130307', '20130308', '20130309', '20130310', '20130311', '20130312', '20130313', '20130314', '20130315', '20130316', '20130317', '20130318', '20130319', '20130320', '20130321', '20130322', '20130323', '20130324', '20130325', '20130326', '20130327', '20130328', '20130329', '20130330', '20130331', '20130401', '20130402', '20130403', '20130404', '20130405', '20130406', '20130407', '20130408', '20130409', '20130410', '20130411', '20130412', '20130413', '20130414', '20130415', '20130416', '20130417', '20130418', '20130419', '20130420', '20130421', '20130422', '20130423', '20130424', '20130425', '20130426', '20130427', '20130428', '20130429', '20130430', '20130501', '20130502', '20130503', '20130504', '20130505', '20130506', '20130507', '20130508', '20130509', '20130510', '20130511', '20130512', '20130513', '20130514', '20130515', '20130516', '20130517', '20130518', '20130519', '20130520', '20130521', '20130522', '20130523', '20130524', '20130525', '20130526', '20130527', '20130528', '20130529', '20130530', '20130531', '20130601', '20130602', '20130603', '20130604', '20130605', '20130606', '20130607', '20130608', '20130609', '20130610', '20130611', '20130612', '20130613', '20130614', '20130615', '20130616', '20130617', '20130618', '20130619', '20130620', '20130621', '20130622', '20130623', '20130624', '20130625', '20130626', '20130627', '20130628', '20130629', '20130630', '20130701', '20130702', '20130703', '20130704', '20130705', '20130706', '20130707', '20130708', '20130709', '20130710', '20130711', '20130712', '20130713', '20130714', '20130715', '20130716', '20130717', '20130718', '20130719', '20130720', '20130721', '20130722', '20130723', '20130724', '20130725', '20130726', '20130727', '20130728', '20130729', '20130730', '20130731', '20130801', '20130802', '20130803', '20130804', '20130805', '20130806', '20130807', '20130808', '20130809', '20130810', '20130811', '20130812', '20130813', '20130814', '20130815', '20130816', '20130817', '20130818', '20130819', '20130820', '20130821', '20130822', '20130823', '20130824', '20130825', '20130826', '20130827', '20130828', '20130829', '20130830', '20130831', '20130901', '20130902', '20130903', '20130904', '20130905', '20130906', '20130907', '20130908', '20130909', '20130910', '20130911', '20130912', '20130913', '20130914', '20130915', '20130916', '20130917', '20130918', '20130919', '20130920', '20130921', '20130922', '20130923', '20130924', '20130925', '20130926', '20130927', '20130928', '20130929', '20130930', '20131001', '20131002', '20131003', '20131004', '20131005', '20131006', '20131007', '20131008', '20131009', '20131010', '20131011', '20131012', '20131013', '20131014', '20131015', '20131016', '20131017', '20131018', '20131019', '20131020', '20131021', '20131022', '20131023', '20131024', '20131025', '20131026', '20131027', '20131028', '20131029', '20131030', '20131031', '20131101', '20131102', '20131103', '20131104', '20131105', '20131106', '20131107', '20131108', '20131109', '20131110', '20131111', '20131112', '20131113', '20131114', '20131115', '20131116', '20131117', '20131118', '20131119', '20131120', '20131121', '20131122', '20131123', '20131124', '20131125', '20131126', '20131127', '20131128', '20131129', '20131130', '20131201', '20131202', '20131203', '20131204', '20131205', '20131206', '20131207', '20131208', '20131209', '20131210', '20131211', '20131212', '20131213', '20131214', '20131215', '20131216', '20131217', '20131218', '20131219', '20131220', '20131221', '20131222', '20131223', '20131224', '20131225', '20131226', '20131227', '20131228', '20131229', '20131230', '20131231', '20140101', '20140102', '20140103', '20140104', '20140105', '20140106', '20140107', '20140108', '20140109', '20140110', '20140111', '20140112', '20140113', '20140114', '20140115', '20140116', '20140117', '20140118', '20140119', '20140120', '20140121', '20140122', '20140123', '20140124', '20140125', '20140126', '20140127', '20140128', '20140129', '20140130', '20140131', '20140201', '20140202', '20140203', '20140204', '20140205', '20140206', '20140207', '20140208', '20140209', '20140210', '20140211', '20140212', '20140213', '20140214', '20140215', '20140216', '20140217', '20140218', '20140219', '20140220', '20140221', '20140222', '20140223', '20140224', '20140225', '20140226', '20140227', '20140228', '20140301', '20140302', '20140303', '20140304', '20140305', '20140306', '20140307', '20140308', '20140309', '20140310', '20140311', '20140312', '20140313', '20140314', '20140315', '20140316', '20140317', '20140318', '20140319', '20140320', '20140321', '20140322', '20140323', '20140324', '20140325', '20140326', '20140327', '20140328', '20140329', '20140330', '20140331', '20140401', '20140402', '20140403', '20140404', '20140405', '20140406', '20140407', '20140408', '20140409', '20140410', '20140411', '20140412', '20140413', '20140414', '20140415', '20140416', '20140417', '20140418', '20140419', '20140420', '20140421', '20140422', '20140423', '20140424', '20140425', '20140426', '20140427', '20140428', '20140429', '20140430', '20140501', '20140502', '20140503', '20140504', '20140505', '20140506', '20140507', '20140508', '20140509', '20140510', '20140511', '20140512', '20140513', '20140514', '20140515', '20140516', '20140517', '20140518', '20140519', '20140520', '20140521', '20140522', '20140523', '20140524', '20140525', '20140526', '20140527', '20140528', '20140529', '20140530', '20140531', '20140601', '20140602', '20140603', '20140604', '20140605', '20140606', '20140607', '20140608', '20140609', '20140610', '20140611', '20140612', '20140613', '20140614', '20140615', '20140616', '20140617', '20140618', '20140619', '20140620', '20140621', '20140622', '20140623', '20140624', '20140625', '20140626', '20140627', '20140628', '20140629', '20140630', '20140701', '20140702', '20140703', '20140704', '20140705', '20140706', '20140707', '20140708', '20140709', '20140710', '20140711', '20140712', '20140713', '20140714', '20140715', '20140716', '20140717', '20140718', '20140719', '20140720', '20140721', '20140722', '20140723', '20140724', '20140725', '20140726', '20140727', '20140728', '20140729', '20140730', '20140731', '20140801', '20140802', '20140803', '20140804', '20140805', '20140806', '20140807', '20140808', '20140809', '20140810', '20140811', '20140812', '20140813', '20140814', '20140815', '20140816', '20140817', '20140818', '20140819', '20140820', '20140821', '20140822', '20140823', '20140824', '20140825', '20140826', '20140827', '20140828', '20140829', '20140830', '20140831', '20140901', '20140902', '20140903', '20140904', '20140905', '20140906', '20140907', '20140908', '20140909', '20140910', '20140911', '20140912', '20140913', '20140914', '20140915', '20140916', '20140917', '20140918', '20140919', '20140920', '20140921', '20140922', '20140923', '20140924', '20140925', '20140926', '20140927', '20140928', '20140929', '20140930', '20141001', '20141002', '20141003', '20141004', '20141005', '20141006', '20141007', '20141008', '20141009', '20141010', '20141011', '20141012', '20141013', '20141014', '20141015', '20141016', '20141017', '20141018', '20141019', '20141020', '20141021', '20141022', '20141023', '20141024', '20141025', '20141026', '20141027', '20141028', '20141029', '20141030', '20141031', '20141101', '20141102', '20141103', '20141104', '20141105', '20141106', '20141107', '20141108', '20141109', '20141110', '20141111', '20141112', '20141113', '20141114', '20141115', '20141116', '20141117', '20141118', '20141119', '20141120', '20141121', '20141122', '20141123', '20141124', '20141125', '20141126', '20141127', '20141128', '20141129', '20141130', '20141201', '20141202', '20141203', '20141204', '20141205', '20141206', '20141207', '20141208', '20141209', '20141210', '20141211', '20141212', '20141213', '20141214', '20141215', '20141216', '20141217', '20141218', '20141219', '20141220', '20141221', '20141222', '20141223', '20141224', '20141225', '20141226', '20141227', '20141228', '20141229', '20141230', '20141231', '20150101', '20150102', '20150103', '20150104', '20150105', '20150106', '20150107', '20150108', '20150109', '20150110', '20150111', '20150112', '20150113', '20150114', '20150115', '20150116', '20150117', '20150118', '20150119', '20150120', '20150121', '20150122', '20150123', '20150124', '20150125', '20150126', '20150127', '20150128', '20150129', '20150130', '20150131', '20150201', '20150202', '20150203', '20150204', '20150205', '20150206', '20150207', '20150208', '20150209', '20150210', '20150211', '20150212', '20150213', '20150214', '20150215', '20150216', '20150217', '20150218', '20150219', '20150220', '20150221', '20150222', '20150223', '20150224', '20150225', '20150226', '20150227', '20150228', '20150301', '20150302', '20150303', '20150304', '20150305', '20150306', '20150307', '20150308', '20150309', '20150310', '20150311', '20150312', '20150313', '20150314', '20150315', '20150316', '20150317', '20150318', '20150319', '20150320', '20150321', '20150322', '20150323', '20150324', '20150325', '20150326', '20150327', '20150328', '20150329', '20150330', '20150331', '20150401', '20150402', '20150403', '20150404', '20150405', '20150406', '20150407', '20150408', '20150409', '20150410', '20150411', '20150412', '20150413', '20150414', '20150415', '20150416', '20150417', '20150418', '20150419', '20150420', '20150421', '20150422', '20150423', '20150424', '20150425', '20150426', '20150427', '20150428', '20150429', '20150430', '20150501', '20150502', '20150503', '20150504', '20150505', '20150506', '20150507', '20150508', '20150509', '20150510', '20150511', '20150512', '20150513', '20150514', '20150515', '20150516', '20150517', '20150518', '20150519', '20150520', '20150521', '20150522', '20150523', '20150524', '20150525', '20150526', '20150527', '20150528', '20150529', '20150530', '20150531', '20150601', '20150602', '20150603', '20150604', '20150605', '20150606', '20150607', '20150608', '20150609', '20150610', '20150611', '20150612', '20150613', '20150614', '20150615', '20150616', '20150617', '20150618', '20150619', '20150620', '20150621', '20150622', '20150623', '20150624', '20150625', '20150626', '20150627', '20150628', '20150629', '20150630', '20150701', '20150702', '20150703', '20150704', '20150705', '20150706', '20150707', '20150708', '20150709', '20150710', '20150711', '20150712', '20150713', '20150714', '20150715', '20150716', '20150717', '20150718', '20150719', '20150720', '20150721', '20150722', '20150723', '20150724', '20150725', '20150726', '20150727', '20150728', '20150729', '20150730', '20150731', '20150801', '20150802', '20150803', '20150804', '20150805', '20150806', '20150807', '20150808', '20150809', '20150810', '20150811', '20150812', '20150813', '20150814', '20150815', '20150816', '20150817', '20150818', '20150819', '20150820', '20150821', '20150822', '20150823', '20150824', '20150825', '20150826', '20150827', '20150828', '20150829', '20150830', '20150831', '20150901', '20150902', '20150903', '20150904', '20150905', '20150906', '20150907', '20150908', '20150909', '20150910', '20150911', '20150912', '20150913', '20150914', '20150915', '20150916', '20150917', '20150918', '20150919', '20150920', '20150921', '20150922', '20150923', '20150924', '20150925', '20150926', '20150927', '20150928', '20150929', '20150930', '20151001', '20151002', '20151003', '20151004', '20151005', '20151006', '20151007', '20151008', '20151009', '20151010', '20151011', '20151012', '20151013', '20151014', '20151015', '20151016', '20151017', '20151018', '20151019', '20151020', '20151021', '20151022', '20151023', '20151024', '20151025', '20151026', '20151027', '20151028', '20151029', '20151030', '20151031', '20151101', '20151102', '20151103', '20151104', '20151105', '20151106', '20151107', '20151108', '20151109', '20151110', '20151111', '20151112', '20151113', '20151114', '20151115', '20151116', '20151117', '20151118', '20151119', '20151120', '20151121', '20151122', '20151123', '20151124', '20151125', '20151126', '20151127', '20151128', '20151129', '20151130', '20151201', '20151202', '20151203', '20151204', '20151205', '20151206', '20151207', '20151208', '20151209', '20151210', '20151211', '20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218', '20151219', '20151220', '20151221', '20151222', '20151223', '20151224', '20151225', '20151226', '20151227', '20151228', '20151229', '20151230', '20151231', '20160101', '20160102', '20160103', '20160104', '20160105', '20160106', '20160107', '20160108', '20160109', '20160110', '20160111', '20160112', '20160113', '20160114', '20160115', '20160116', '20160117', '20160118', '20160119', '20160120', '20160121', '20160122', '20160123', '20160124', '20160125', '20160126', '20160127', '20160128', '20160129', '20160130', '20160131', '20160201', '20160202', '20160203', '20160204', '20160205', '20160206', '20160207', '20160208', '20160209', '20160210', '20160211', '20160212', '20160213', '20160214', '20160215', '20160216', '20160217', '20160218', '20160219', '20160220', '20160221', '20160222', '20160223', '20160224', '20160225', '20160226', '20160227', '20160228', '20160229', '20160301', '20160302', '20160303', '20160304', '20160305', '20160306', '20160307', '20160308', '20160309', '20160310', '20160311', '20160312', '20160313', '20160314', '20160315', '20160316', '20160317', '20160318', '20160319', '20160320', '20160321', '20160322', '20160323', '20160324', '20160325', '20160326', '20160327', '20160328', '20160329', '20160330', '20160331', '20160401', '20160402', '20160403', '20160404', '20160405', '20160406', '20160407', '20160408', '20160409', '20160410', '20160411', '20160412', '20160413', '20160414', '20160415', '20160416', '20160417', '20160418', '20160419', '20160420', '20160421', '20160422', '20160423', '20160424', '20160425', '20160426', '20160427', '20160428', '20160429', '20160430', '20160501', '20160502', '20160503', '20160504', '20160505', '20160506', '20160507', '20160508', '20160509', '20160510', '20160511', '20160512', '20160513', '20160514', '20160515', '20160516', '20160517', '20160518', '20160519', '20160520', '20160521', '20160522', '20160523', '20160524', '20160525', '20160526', '20160527', '20160528', '20160529', '20160530', '20160531', '20160601', '20160602', '20160603', '20160604', '20160605', '20160606', '20160607', '20160608', '20160609', '20160610', '20160611', '20160612', '20160613', '20160614', '20160615', '20160616', '20160617', '20160618', '20160619', '20160620', '20160621', '20160622', '20160623', '20160624', '20160625', '20160626', '20160627', '20160628', '20160629', '20160630', '20160701', '20160702', '20160703', '20160704', '20160705', '20160706', '20160707', '20160708', '20160709', '20160710', '20160711', '20160712', '20160713', '20160714', '20160715', '20160716', '20160717', '20160718', '20160719', '20160720', '20160721', '20160722', '20160723', '20160724', '20160725', '20160726', '20160727', '20160728', '20160729', '20160730', '20160731', '20160801', '20160802', '20160803', '20160804', '20160805', '20160806', '20160807', '20160808', '20160809', '20160810', '20160811', '20160812', '20160813', '20160814', '20160815', '20160816', '20160817', '20160818', '20160819', '20160820', '20160821', '20160822', '20160823', '20160824', '20160825', '20160826', '20160827', '20160828', '20160829', '20160830', '20160831', '20160901', '20160902', '20160903', '20160904', '20160905', '20160906', '20160907', '20160908', '20160909', '20160910', '20160911', '20160912', '20160913', '20160914', '20160915', '20160916', '20160917', '20160918', '20160919', '20160920', '20160921', '20160922', '20160923', '20160924', '20160925', '20160926', '20160927', '20160928', '20160929', '20160930', '20161001', '20161002', '20161003', '20161004', '20161005', '20161006', '20161007', '20161008', '20161009', '20161010', '20161011', '20161012', '20161013', '20161014', '20161015', '20161016', '20161017', '20161018', '20161019', '20161020', '20161021', '20161022', '20161023', '20161024', '20161025', '20161026', '20161027', '20161028', '20161029', '20161030', '20161031', '20161101', '20161102', '20161103', '20161104', '20161105', '20161106', '20161107', '20161108', '20161109', '20161110', '20161111', '20161112', '20161113', '20161114', '20161115', '20161116', '20161117', '20161118', '20161119', '20161120', '20161121', '20161122', '20161123', '20161124', '20161125', '20161126', '20161127', '20161128', '20161129', '20161130', '20161201', '20161202', '20161203', '20161204', '20161205', '20161206', '20161207', '20161208', '20161209', '20161210', '20161211', '20161212', '20161213', '20161214', '20161215', '20161216', '20161217', '20161218', '20161219', '20161220', '20161221', '20161222', '20161223', '20161224', '20161225', '20161226', '20161227', '20161228', '20161229', '20161230', '20161231', '20170101', '20170102', '20170103', '20170104', '20170105', '20170106', '20170107', '20170108', '20170109', '20170110', '20170111', '20170112', '20170113', '20170114', '20170115', '20170116', '20170117', '20170118', '20170119', '20170120', '20170121', '20170122', '20170123', '20170124', '20170125', '20170126', '20170127', '20170128', '20170129', '20170130', '20170131', '20170201', '20170202', '20170203', '20170204', '20170205', '20170206', '20170207', '20170208', '20170209', '20170210', '20170211', '20170212', '20170213', '20170214', '20170215', '20170216', '20170217', '20170218', '20170219', '20170220', '20170221', '20170222', '20170223', '20170224', '20170225', '20170226', '20170227', '20170228', '20170301', '20170302', '20170303', '20170304', '20170305', '20170306', '20170307', '20170308', '20170309', '20170310', '20170311', '20170312', '20170313', '20170314', '20170315', '20170316', '20170317', '20170318', '20170319', '20170320', '20170321', '20170322', '20170323', '20170324', '20170325', '20170326', '20170327', '20170328', '20170329', '20170330', '20170331', '20170401', '20170402', '20170403', '20170404', '20170405', '20170406', '20170407', '20170408', '20170409', '20170410', '20170411', '20170412', '20170413', '20170414', '20170415', '20170416', '20170417', '20170418', '20170419', '20170420', '20170421', '20170422', '20170423', '20170424', '20170425', '20170426', '20170427', '20170428', '20170429', '20170430', '20170501', '20170502', '20170503', '20170504', '20170505', '20170506', '20170507', '20170508', '20170509', '20170510', '20170511', '20170512', '20170513', '20170514', '20170515', '20170516', '20170517', '20170518', '20170519', '20170520', '20170521', '20170522', '20170523', '20170524', '20170525', '20170526', '20170527', '20170528', '20170529', '20170530', '20170531', '20170601', '20170602', '20170603', '20170604', '20170605', '20170606', '20170607', '20170608', '20170609', '20170610', '20170611', '20170612', '20170613', '20170614', '20170615', '20170616', '20170617', '20170618', '20170619', '20170620', '20170621', '20170622', '20170623', '20170624', '20170625', '20170626', '20170627', '20170628', '20170629', '20170630', '20170701', '20170702', '20170703', '20170704', '20170705', '20170706', '20170707', '20170708', '20170709', '20170710', '20170711', '20170712', '20170713', '20170714', '20170715', '20170716', '20170717', '20170718', '20170719', '20170720', '20170721', '20170722', '20170723', '20170724', '20170725', '20170726', '20170727', '20170728', '20170729', '20170730', '20170731', '20170801', '20170802', '20170803', '20170804', '20170805', '20170806', '20170807', '20170808', '20170809', '20170810', '20170811', '20170812', '20170813', '20170814', '20170815', '20170816', '20170817', '20170818', '20170819', '20170820', '20170821', '20170822', '20170823', '20170824', '20170825', '20170826', '20170827', '20170828', '20170829', '20170830', '20170831', '20170901', '20170902', '20170903', '20170904', '20170905', '20170906', '20170907', '20170908', '20170909', '20170910', '20170911', '20170912', '20170913', '20170914', '20170915', '20170916', '20170917', '20170918', '20170919', '20170920', '20170921', '20170922', '20170923', '20170924', '20170925', '20170926', '20170927', '20170928', '20170929', '20170930', '20171001', '20171002', '20171003', '20171004', '20171005', '20171006', '20171007', '20171008', '20171009', '20171010', '20171011', '20171012', '20171013', '20171014', '20171015', '20171016', '20171017', '20171018', '20171019', '20171020', '20171021', '20171022', '20171023', '20171024', '20171025', '20171026', '20171027', '20171028', '20171029', '20171030', '20171031', '20171101', '20171102', '20171103', '20171104', '20171105', '20171106', '20171107', '20171108', '20171109', '20171110', '20171111', '20171112', '20171113', '20171114', '20171115', '20171116', '20171117', '20171118', '20171119', '20171120', '20171121', '20171122', '20171123', '20171124', '20171125', '20171126', '20171127', '20171128', '20171129', '20171130', '20171201', '20171202', '20171203', '20171204', '20171205', '20171206', '20171207', '20171208', '20171209', '20171210', '20171211', '20171212', '20171213', '20171214', '20171215', '20171216', '20171217', '20171218', '20171219', '20171220', '20171221', '20171222', '20171223', '20171224', '20171225', '20171226', '20171227', '20171228', '20171229', '20171230', '20171231', '20180101', '20180102', '20180103', '20180104', '20180105', '20180106', '20180107', '20180108', '20180109', '20180110', '20180111', '20180112', '20180113', '20180114', '20180115', '20180116', '20180117', '20180118', '20180119', '20180120', '20180121', '20180122', '20180123', '20180124', '20180125', '20180126', '20180127', '20180128', '20180129', '20180130', '20180131', '20180201', '20180202', '20180203', '20180204', '20180205', '20180206', '20180207', '20180208', '20180209', '20180210', '20180211', '20180212', '20180213', '20180214', '20180215', '20180216', '20180217', '20180218', '20180219', '20180220', '20180221', '20180222', '20180223', '20180224', '20180225', '20180226', '20180227', '20180228', '20180301', '20180302', '20180303', '20180304', '20180305', '20180306', '20180307', '20180308', '20180309', '20180310', '20180311', '20180312', '20180313', '20180314', '20180315', '20180316', '20180317', '20180318', '20180319', '20180320', '20180321', '20180322', '20180323', '20180324', '20180325', '20180326', '20180327', '20180328', '20180329', '20180330', '20180331', '20180401', '20180402', '20180403', '20180404', '20180405', '20180406', '20180407', '20180408', '20180409', '20180410', '20180411', '20180412', '20180413', '20180414', '20180415', '20180416', '20180417', '20180418', '20180419', '20180420', '20180421', '20180422', '20180423', '20180424', '20180425', '20180426', '20180427', '20180428', '20180429', '20180430', '20180501', '20180502', '20180503', '20180504', '20180505', '20180506', '20180507', '20180508', '20180509', '20180510', '20180511', '20180512', '20180513', '20180514', '20180515', '20180516', '20180517', '20180518', '20180519', '20180520', '20180521', '20180522', '20180523', '20180524', '20180525', '20180526', '20180527', '20180528', '20180529', '20180530', '20180531', '20180601', '20180602', '20180603', '20180604', '20180605', '20180606', '20180607', '20180608', '20180609', '20180610', '20180611', '20180612', '20180613', '20180614', '20180615', '20180616', '20180617', '20180618', '20180619', '20180620', '20180621', '20180622', '20180623', '20180624', '20180625', '20180626', '20180627', '20180628', '20180629', '20180630', '20180701', '20180702', '20180703', '20180704', '20180705', '20180706', '20180707', '20180708', '20180709', '20180710', '20180711', '20180712', '20180713', '20180714', '20180715', '20180716', '20180717', '20180718', '20180719', '20180720', '20180721', '20180722', '20180723', '20180724', '20180725', '20180726', '20180727', '20180728', '20180729', '20180730', '20180731', '20180801', '20180802', '20180803', '20180804', '20180805', '20180806', '20180807', '20180808', '20180809', '20180810', '20180811', '20180812', '20180813', '20180814', '20180815', '20180816', '20180817', '20180818', '20180819', '20180820', '20180821', '20180822', '20180823', '20180824', '20180825', '20180826', '20180827', '20180828', '20180829', '20180830', '20180831', '20180901', '20180902', '20180903', '20180904', '20180905', '20180906', '20180907', '20180908', '20180909', '20180910', '20180911', '20180912', '20180913', '20180914', '20180915', '20180916', '20180917', '20180918', '20180919', '20180920', '20180921', '20180922', '20180923', '20180924', '20180925', '20180926', '20180927', '20180928', '20180929', '20180930', '20181001', '20181002', '20181003', '20181004', '20181005', '20181006', '20181007', '20181008', '20181009', '20181010', '20181011', '20181012', '20181013', '20181014', '20181015', '20181016', '20181017', '20181018', '20181019', '20181020', '20181021', '20181022', '20181023', '20181024', '20181025', '20181026', '20181027', '20181028', '20181029', '20181030', '20181031', '20181101', '20181102', '20181103', '20181104', '20181105', '20181106', '20181107', '20181108', '20181109', '20181110', '20181111', '20181112', '20181113', '20181114', '20181115', '20181116', '20181117', '20181118', '20181119', '20181120', '20181121', '20181122', '20181123', '20181124', '20181125', '20181126', '20181127', '20181128', '20181129', '20181130', '20181201', '20181202', '20181203', '20181204', '20181205', '20181206', '20181207', '20181208', '20181209', '20181210', '20181211', '20181212', '20181213', '20181214', '20181215', '20181216', '20181217', '20181218', '20181219', '20181220', '20181221', '20181222', '20181223', '20181224', '20181225', '20181226', '20181227', '20181228', '20181229', '20181230', '20181231', '20190101', '20190102', '20190103', '20190104', '20190105', '20190106', '20190107', '20190108', '20190109', '20190110', '20190111', '20190112', '20190113', '20190114', '20190115', '20190116', '20190117', '20190118', '20190119', '20190120', '20190121', '20190122', '20190123', '20190124', '20190125', '20190126', '20190127', '20190128', '20190129', '20190130', '20190131', '20190201', '20190202', '20190203', '20190204', '20190205', '20190206', '20190207', '20190208', '20190209', '20190210', '20190211', '20190212', '20190213', '20190214', '20190215', '20190216', '20190217', '20190218', '20190219', '20190220', '20190221', '20190222', '20190223', '20190224', '20190225', '20190226', '20190227', '20190228', '20190301', '20190302', '20190303', '20190304', '20190305', '20190306', '20190307', '20190308', '20190309', '20190310', '20190311', '20190312', '20190313', '20190314', '20190315', '20190316', '20190317', '20190318', '20190319', '20190320', '20190321', '20190322', '20190323', '20190324', '20190325', '20190326', '20190327']
    base_url = 'https://interface.meiriyiwen.com/article/day?date='
    start_urls = [base_url+alldays[0]]       
   
    def parse(self, response):
        self.offsize += 1
        print('asdasdasdsadasdasdasdas',response.status)
        if (response.status == 404):
            print('...........................',response.status, self.offsize)
            return scrapy.Request(self.base_url + str(self.alldays[self.offsize]), callback=self.parse)

        douyu_data = json.loads(response.body)['data']
        if (len(douyu_data)>0):
            author = pymysql.escape_string(douyu_data['author'])
            title = pymysql.escape_string(douyu_data['title'])
            digest = pymysql.escape_string(douyu_data['digest'])
            content = pymysql.escape_string(douyu_data['content'])
            print('......................', title)
            if (len(content) < 20000):
                db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
                cursor = db.cursor()
                sql = """INSERT INTO wenzhan values ('%s', '%s', '%s', '%s')"""%(author, title, digest, content)
                cursor.execute(sql)
                db.commit()
                db.close()

        yield scrapy.Request(self.base_url + str(self.alldays[self.offsize]), callback=self.parse)
