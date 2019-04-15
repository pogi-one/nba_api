import nba_api.stats.endpoints as ep

class DeferredEndpoint:
    '''Simple class to represent an endpoint with deferred evaluation.'''
    def __init__(self, endpoint_class, **kwargs):
        self.endpoint_class = endpoint_class
        self.kwargs = kwargs

    def __call__(self):
        return self.endpoint_class(**self.kwargs)

# A bunch of valid but uninstantiated endpoints for testing:
deferred_endpoints = [
        DeferredEndpoint(ep.AssistLeaders),
        DeferredEndpoint(ep.AssistTracker),
        DeferredEndpoint(ep.BoxScoreAdvancedV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreDefensive, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreFourFactorsV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreMatchups, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreMiscV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScorePlayerTrackV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreScoringV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreSummaryV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreTraditionalV2, game_id='0021700807'),
        DeferredEndpoint(ep.BoxScoreUsageV2, game_id='0021700807'),
        DeferredEndpoint(ep.CommonAllPlayers),
        DeferredEndpoint(ep.CommonPlayerInfo, player_id='2544'),
        DeferredEndpoint(ep.CommonPlayoffSeries),
        DeferredEndpoint(ep.CommonTeamRoster, team_id='1610612739'),
        DeferredEndpoint(ep.CommonTeamYears),
        DeferredEndpoint(ep.DefenseHub, season='2017-18'),
        DeferredEndpoint(ep.DraftCombineDrillResults),
        DeferredEndpoint(ep.DraftCombineNonStationaryShooting),
        DeferredEndpoint(ep.DraftCombinePlayerAnthro),
        DeferredEndpoint(ep.DraftCombineSpotShooting),
        DeferredEndpoint(ep.DraftCombineStats),
        DeferredEndpoint(ep.DraftHistory),
        DeferredEndpoint(ep.FantasyWidget),
        DeferredEndpoint(ep.FranchiseHistory),
        DeferredEndpoint(ep.FranchiseLeaders, team_id='1610612739'),
        DeferredEndpoint(ep.FranchisePlayers, team_id='1610612739'),
        DeferredEndpoint(ep.HomePageLeaders),
        DeferredEndpoint(ep.HomePageV2),
        DeferredEndpoint(ep.InfographicFanDuelPlayer, game_id='0021700807'),
        DeferredEndpoint(ep.LeadersTiles),
        DeferredEndpoint(ep.LeagueDashLineups),
        DeferredEndpoint(ep.LeagueDashPlayerBioStats),
        DeferredEndpoint(ep.LeagueDashPlayerClutch),
        DeferredEndpoint(ep.LeagueDashPlayerPtShot),
        DeferredEndpoint(ep.LeagueDashPlayerShotLocations),
        DeferredEndpoint(ep.LeagueDashPlayerStats),
        DeferredEndpoint(ep.LeagueDashPtDefend),
        DeferredEndpoint(ep.LeagueDashPtStats),
        DeferredEndpoint(ep.LeagueDashPtTeamDefend),
        DeferredEndpoint(ep.LeagueDashTeamClutch),
        DeferredEndpoint(ep.LeagueDashTeamPtShot),
        DeferredEndpoint(ep.LeagueDashTeamShotLocations),
        DeferredEndpoint(ep.LeagueDashTeamStats),
        DeferredEndpoint(ep.LeagueGameFinder),
        DeferredEndpoint(ep.LeagueGameLog),
        DeferredEndpoint(ep.LeagueLeaders),
        DeferredEndpoint(ep.LeaguePlayerOnDetails, team_id='1610612739'),
        DeferredEndpoint(ep.LeagueSeasonMatchups, off_player_id_nullable=2544,
            def_player_id_nullable='1610612739'),
        DeferredEndpoint(ep.LeagueStandings),
        DeferredEndpoint(ep.PlayByPlay, game_id='0021700807'),
        DeferredEndpoint(ep.PlayByPlayV2, game_id='0021700807'),
        DeferredEndpoint(ep.PlayerAwards, player_id='2544'),
        DeferredEndpoint(ep.PlayerCareerStats, player_id='2544'),
        DeferredEndpoint(ep.PlayerCompare, player_id_list='202681,203078,2544,201567,203954',
                vs_player_id_list='201566,201939,201935,201142,203076'),
        DeferredEndpoint(ep.PlayerDashPtPass, player_id='2544', team_id='1610612739'),
        DeferredEndpoint(ep.PlayerDashPtReb, player_id='2544', team_id='1610612739'),
        DeferredEndpoint(ep.PlayerDashPtShotDefend, player_id='2544',
                team_id='1610612739'),
        DeferredEndpoint(ep.PlayerDashPtShots, player_id='2544', team_id='1610612739'),
        DeferredEndpoint(ep.PlayerDashboardByClutch, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByGameSplits, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByGeneralSplits, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByLastNGames, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByOpponent, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByShootingSplits, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByTeamPerformance, player_id='2544'),
        DeferredEndpoint(ep.PlayerDashboardByYearOverYear, player_id='2544'),
        DeferredEndpoint(ep.PlayerFantasyProfile, player_id='2544'),
        DeferredEndpoint(ep.PlayerFantasyProfileBarGraph, player_id='2544'),
        DeferredEndpoint(ep.PlayerGameLog, player_id='2544'),
        DeferredEndpoint(ep.PlayerGameStreakFinder),
        DeferredEndpoint(ep.PlayerNextNGames, player_id='2544'),
        DeferredEndpoint(ep.PlayerProfileV2, player_id='2544'),
        DeferredEndpoint(ep.PlayerVsPlayer, player_id='2544', vs_player_id='202681'),
        DeferredEndpoint(ep.PlayoffPicture),
        DeferredEndpoint(ep.Scoreboard),
        DeferredEndpoint(ep.ScoreboardV2),
        DeferredEndpoint(ep.ShotChartDetail, player_id='2544', team_id='1610612739'),
        DeferredEndpoint(ep.ShotChartLineupDetail),
        DeferredEndpoint(ep.SynergyPlayTypes),
        DeferredEndpoint(ep.TeamAndPlayersVsPlayers,
                team_id=1610612739,
                player_id1=203954,
                player_id2=201567,
                player_id3=203507,
                player_id4=203078,
                player_id5=202681,
                vs_team_id=1610612765,
                vs_player_id1=203954,
                vs_player_id2=201567,
                vs_player_id3=203507,
                vs_player_id4=203078,
                vs_player_id5=202681),
        DeferredEndpoint(ep.TeamDashLineups, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashPtPass, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashPtReb, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashPtShots, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByClutch, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByGameSplits, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByGeneralSplits, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByLastNGames, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByOpponent, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByShootingSplits, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByTeamPerformance, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDashboardByYearOverYear, team_id='1610612739'),
        DeferredEndpoint(ep.TeamDetails, team_id='1610612739'),
        DeferredEndpoint(ep.TeamGameLog, team_id='1610612739'),
        DeferredEndpoint(ep.TeamGameStreakFinder),
        DeferredEndpoint(ep.TeamHistoricalLeaders, team_id='1610612739'),
        DeferredEndpoint(ep.TeamInfoCommon, team_id='1610612739'),
        DeferredEndpoint(ep.TeamPlayerDashboard, team_id='1610612739'),
        DeferredEndpoint(ep.TeamPlayerOnOffDetails, team_id='1610612739'),
        DeferredEndpoint(ep.TeamPlayerOnOffSummary, team_id='1610612739'),
        DeferredEndpoint(ep.TeamVsPlayer, team_id='1610612739', vs_player_id='2544'),
        DeferredEndpoint(ep.TeamYearByYearStats, team_id='1610612739'),
        DeferredEndpoint(ep.VideoDetails, player_id='2544', game_id='0021700807',
                team_id='1610612739', start_period=1, end_period=1),
        DeferredEndpoint(ep.VideoEvents, game_id='0021700807'),
        DeferredEndpoint(ep.VideoStatus),
        DeferredEndpoint(ep.WinProbabilityPBP, game_id='0021700807')
]
